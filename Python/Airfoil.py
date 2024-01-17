# SOURCE/VORTEX PANEL METHOD - SINGLE AIRFOIL
# Based on the files and videos from JoshTheEngineer

import numpy as np
import math as math
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import path

import io
import base64

from COMPUTE_IJ_SPM import COMPUTE_IJ_SPM
from COMPUTE_KL_VPM import COMPUTE_KL_VPM
from STREAMLINE_SPM import STREAMLINE_SPM
from STREAMLINE_VPM import STREAMLINE_VPM
from COMPUTE_CIRCULATION import COMPUTE_CIRCULATION

PLOT = False

def compute(Vinf, AoA, dataBuffer):
    
    text_output = "Vinf: %f\nAoA: %f\n" % (Vinf, AoA)


    # Convert angle of attack to radians
    AoAR = AoA*(np.pi/180)
    
    # Boundary point X-coordinate
    XB = dataBuffer[:,0]
    # Boundary point Y-coordinate
    YB = dataBuffer[:,1]

    # Number of boundary points
    numPts = len(XB)
    # Number of panels (control points)
    numPan = numPts - 1

    # %% CHECK PANEL DIRECTIONS - FLIP IF NECESSARY

    # Check for direction of points
    # Initialize edge value array
    edge = np.zeros(numPan)
    # Loop over all panels
    for i in range(numPan):
        # Compute edge values
        edge[i] = (XB[i+1]-XB[i])*(YB[i+1]+YB[i])

    # Sum all edge values
    sumEdge = np.sum(edge)

    # If panels are CCW, flip them (don't if CW)
    # If panels are CCW
    if (sumEdge < 0):
        # Flip the X-data array
        XB = np.flipud(XB)
        # Flip the Y-data array
        YB = np.flipud(YB)

    # %% PANEL METHOD GEOMETRY

    # Initialize variables
    # Initialize control point X-coordinate array
    XC  = np.zeros(numPan)
    # Initialize control point Y-coordinate array
    YC  = np.zeros(numPan)
    # Initialize panel length array
    S   = np.zeros(numPan)
    # Initialize panel orientation angle array [deg]
    phi = np.zeros(numPan)

    # Find geometric quantities of the airfoil
    # Loop over all panels
    for i in range(numPan):
        # X-value of control point
        XC[i]   = 0.5*(XB[i]+XB[i+1])
        # Y-value of control point
        YC[i]   = 0.5*(YB[i]+YB[i+1])
        # Change in X between boundary points
        dx      = XB[i+1]-XB[i]
        # Change in Y between boundary points
        dy      = YB[i+1]-YB[i]
        # Length of the panel
        S[i]    = (dx**2 + dy**2)**0.5
        # Angle of panel (positive X-axis to inside face)
        phi[i]  = math.atan2(dy,dx)
        # Make all panel angles positive [rad]
        if (phi[i] < 0):
            phi[i] = phi[i] + 2*np.pi

    # Compute angle of panel normal w.r.t. horizontal and include AoA
    # Angle from positive X-axis to outward normal vector [rad]
    delta                = phi + (np.pi/2)
    # Angle between freestream vector and outward normal vector [rad]
    beta                 = delta - AoAR
    # Make all panel angles between 0 and 2pi [rad]
    beta[beta > 2*np.pi] = beta[beta > 2*np.pi] - 2*np.pi

    # %% COMPUTE SOURCE AND VORTEX PANEL STRENGTHS - REF [10]

    # Geometric integrals for SPM and VPM (normal [I,K] and tangential [J,L])
    I, J = COMPUTE_IJ_SPM(XC,YC,XB,YB,phi,S)
    K, L = COMPUTE_KL_VPM(XC,YC,XB,YB,phi,S)

    # Populate A matrix
    A = I + np.pi*np.eye(numPan,numPan)

    # Right column of A matrix
    # Used to enlarge the A matrix to account for gamma column
    newAV = np.zeros((numPan,1))
    # Horizontally stack the A matrix with newAV to get enlarged matrix
    A     = np.hstack((A,newAV))
    # Loop over all i panels (rows)
    for i in range(numPan):
        # Add gamma term to right-most column of A matrix
        A[i,numPan] = -sum(K[i,:])
        
    # Bottom row of A matrix
    # Used to enlarge the A matrix to account for Kutta condition equation
    newAH = np.zeros((1,numPan+1))
    # Vertically stack the A matrix with newAH to get enlarged matrix
    A     = np.vstack((A,newAH))
    # Loop over all j panels (columns)
    for j in range(numPan):
        # Source contribution of Kutta condition equation
        A[numPan,j] = J[0,j] + J[numPan-1,j]
    # Vortex contribution of Kutta condition equation
    A[numPan,numPan] = -(sum(L[0,:] + L[numPan-1,:])) + 2*np.pi

    # Populate b array
    b = -Vinf*2*np.pi*np.cos(beta)

    # Last element of b array (Kutta condition)
    # Add Kutta condition equation RHS to b array
    b = np.append(b,-Vinf*2*np.pi*(np.sin(beta[0]) + np.sin(beta[numPan-1])))

    # Compute result array
    # Solve system of equation for all source strengths and single vortex strength
    resArr = np.linalg.solve(A,b)

    # Separate lam and gamma values from result 
    # All panel source strengths
    lam   = resArr[0:len(resArr)-1]
    # Constant vortex strength
    gamma = resArr[len(resArr)-1]

    # %% COMPUTE PANEL VELOCITIES AND PRESSURE COEFFICIENTS

    # Compute velocities
    # Initialize tangential velocity
    Vt = np.zeros(numPan)
    # Initialize pressure coefficient
    Cp = np.zeros(numPan)
    # Loop over all panels
    for i in range(numPan):
        # Uniform flow term
        term1 = Vinf*np.sin(beta[i])
        # Source panel terms when j is not equal to i
        term2 = (1/(2*np.pi))*sum(lam*J[i,:])
        # Vortex panel term when j is equal to i
        term3 = gamma/2
        # Vortex panel terms when j is not equal to i
        term4 = -(gamma/(2*np.pi))*sum(L[i,:])
        
        # Compute tangential velocity on panel i
        Vt[i] = term1 + term2 + term3 + term4
        # Compute pressure coefficient on panel i
        Cp[i] = 1-(Vt[i]/Vinf)**2

    # %% COMPUTE LIFT AND MOMENT COEFFICIENTS

    # Compute normal and axial force coefficients
    CN = -Cp*S*np.sin(beta)
    CA = -Cp*S*np.cos(beta)

    # Compute lift and moment coefficients
    # Decompose axial and normal to lift coefficient []
    CL = sum(CN*np.cos(AoAR)) - sum(CA*np.sin(AoAR))
    # Moment coefficient []
    CM = sum(Cp*(XC-0.25)*S*np.cos(phi))

    # Print the results to the Console
    print("======= RESULTS =======")
    print("Lift Coefficient (CL)")
    # From this SPVP code
    print("  SPVP : %2.8f" % CL)
    # From Kutta-Joukowski lift equation
    print("  K-J  : %2.8f" % (2*sum(gamma*S)))
    print("Moment Coefficient (CM)")
    print("  SPVP : %2.8f" % CM)

    text_output += "======= RESULTS =======\n"
    text_output += "Lift Coefficient (CL)\n"
    # From this SPVP code
    text_output += "  SPVP : %2.8f\n" % CL
    # From Kutta-Joukowski lift equation
    text_output += "  K-J  : %2.8f\n" % (2*sum(gamma*S))
    text_output += "Moment Coefficient (CM)\n"
    text_output += "  SPVP : %2.8f\n" % CM


    # %% PLOTTING

    # FIGURE: Airfoil with panel normal vectors
    fig = plt.figure(1)
    plt.cla()
    # Plot the airfoil
    plt.fill(XB,YB,'k')
    X = np.zeros(2)
    Y = np.zeros(2)
    # Loop over all panels
    pans = []
    for i in range(numPan):
        # Set X start of panel orientation vector
        X[0] = XC[i]
        # Set X end of panel orientation vector
        X[1] = XC[i] + S[i]*np.cos(delta[i])
        # Set Y start of panel orientation vector
        Y[0] = YC[i]
        # Set Y end of panel orientation vector
        Y[1] = YC[i] + S[i]*np.sin(delta[i])
        # If it's the first panel index
        if (i == 0):
            # Plot normal vector for first panel
            plt.plot(X,Y,'b-',label='First Panel')
        # If it's the second panel index
        elif (i == 1):
            # Plot normal vector for second panel
            plt.plot(X,Y,'g-',label='Second Panel')
        # If it's neither the first nor second panel index
        else:
            # Plot normal vector for all other panels
            plt.plot(X,Y,'r-')
        pans.append([X.tolist(), Y.tolist()])
            
    plt.xlabel('X Units')
    plt.ylabel('Y Units')
    plt.title('Panel Geometry')
    plt.axis('equal')
    plt.legend()

    if PLOT:
        plt.show()
    
    fillData = [XB.tolist(), YB.tolist()]
    # save the plot and convert to base64
    stringBytesIO = io.BytesIO()
    plt.savefig(stringBytesIO, format='png')
    stringBytesIO.seek(0)
    panel_geometry = {"pic": base64.b64encode(stringBytesIO.read()).decode('utf-8'), "data": pans, "fillData": fillData}


    # FIGURE: Geometry with: boundary points, control points, first panel, second panel
    fig = plt.figure(2)
    plt.cla()
    # Plot airfoil panels
    plt.plot(XB,YB,'k-')
    # Plot first panel
    plt.plot([XB[0], XB[1]],[YB[0], YB[1]],'b-',label='First Panel')
    # Plot second panel
    plt.plot([XB[1], XB[2]],[YB[1], YB[2]],'g-',label='Second Panel')
    # Plot boundary points (black circles)
    plt.plot(XB,YB,'ko',markerfacecolor='k',label='Boundary Pts')
    # Plot control points (red circles)
    plt.plot(XC,YC,'ko',markerfacecolor='r',label='Control Pts')
    plt.xlabel('X Units')
    plt.ylabel('Y Units')
    plt.axis('equal')
    plt.legend()
    
    if PLOT:
        plt.show()

    stringBytesIO = io.BytesIO()
    plt.savefig(stringBytesIO, format='png')
    stringBytesIO.seek(0)
    geom_pts = {"pic": base64.b64encode(stringBytesIO.read()).decode('utf-8'), "data": [XC.tolist(), YC.tolist()]}

    # FIGURE: Cp vectors at airfoil control points
    fig = plt.figure(3)
    plt.cla()
    # Scale and make positive all Cp values
    Cps = np.absolute(Cp*0.15)
    X = np.zeros(2)
    Y = np.zeros(2)

    blue = []
    red = []
    # Loop over all panels
    for i in range(len(Cps)):
        # Control point X-coordinate
        X[0] = XC[i]
        # Ending X-value based on Cp magnitude
        X[1] = XC[i] + Cps[i]*np.cos(delta[i])
        # Control point Y-coordinate
        Y[0] = YC[i]
        # Ending Y-value based on Cp magnitude
        Y[1] = YC[i] + Cps[i]*np.sin(delta[i])
        
        # If pressure coefficient is negative
        if (Cp[i] < 0):
            # Plot as a red line
            plt.plot(X,Y,'r-')
            red.append([X.tolist(), Y.tolist()])
        # If pressure coefficient is zero or positive
        elif (Cp[i] >= 0):
            # Plot as a blue line
            plt.plot(X,Y,'b-')
            blue.append([X.tolist(), Y.tolist()])
    # Plot the airfoil as black polygon
    plt.fill(XB,YB,'k')
    plt.xlabel('X Units')
    plt.ylabel('Y Units')
    plt.gca().set_aspect('equal')
    
    if PLOT:
        plt.show()

    stringBytesIO = io.BytesIO()
    plt.savefig(stringBytesIO, format='png')
    stringBytesIO.seek(0)
    control_pts = {"pic": base64.b64encode(stringBytesIO.read()).decode('utf-8'), "data": [blue, red]}


    # FIGURE: Pressure coefficient
    fig = plt.figure(4)
    plt.cla()
    # Airfoil middle index for VPM data
    midIndS = int(np.floor(len(Cp)/2))
    # Plot Cp for upper surface of airfoil from panel method
    plt.plot(XC[midIndS+1:len(XC)],Cp[midIndS+1:len(XC)],'ks',markerfacecolor='b',label='VPM Upper')
    # Plot Cp for lower surface of airfoil from panel method
    plt.plot(XC[0:midIndS],Cp[0:midIndS],'ks',markerfacecolor='r',label='VPM Lower')
    plt.xlim(0,1)
    plt.xlabel('X Coordinate')
    plt.ylabel('Cp')
    plt.title('Pressure Coefficient')
    if PLOT:
        plt.show()

    plt.legend()
    # Invert Cp (Y) axis
    plt.gca().invert_yaxis()
    vpmUpper = [XC[midIndS+1:len(XC)].tolist(), Cp[midIndS+1:len(XC)].tolist()]
    vpmLower = [XC[0:midIndS].tolist(), Cp[0:midIndS].tolist()]

    stringBytesIO = io.BytesIO()
    plt.savefig(stringBytesIO, format='png')
    stringBytesIO.seek(0)
    pressure = {"pic": base64.b64encode(stringBytesIO.read()).decode('utf-8'), "data": [vpmUpper, vpmLower]}
      
    return text_output, panel_geometry, geom_pts, control_pts, pressure