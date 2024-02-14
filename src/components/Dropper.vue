<template>
    <div class="container mx-auto px-4">
      <h1 class="text-xl font-bold pt-4">A dropdown menu component using floating-vue and Tailwind</h1>
  
      <div class="grid grid-cols-2">
        <div>
          <div class="mt-4">Using a list of links</div>
          <div class="mt-4">
            <Dropdown class="inline" popper-class="w-64 bg-white border rounded-lg shadow-md">
              <!-- Dropdown trigger -->
              <button
                class="
                  dropdown-trigger
                  inline-block
                  px-6
                  py-3
                  bg-blue-600
                  text-white
                  leading-tight
                  rounded
                  hover:bg-blue-700
                  focus:bg-blue-700 focus:outline-none focus:ring-0
                  active:bg-blue-800
                  transition
                  duration-150
                  ease-in-out
                "
              >
                Dropdown button
              </button>
  
              <!-- Dropdown content -->
              <template #popper="{ hide }">
                <ul class="py-1 text-gray-70">
                  <li>
                    <a href="#" class="block py-2 px-4 hover:bg-gray-100 focus:bg-gray-100 outline-none" @click="hide">Click me to close</a>
                  </li>
                  <li>
                    <a href="#" class="block py-2 px-4 hover:bg-gray-100 focus:bg-gray-100 outline-none">Menu item</a>
                  </li>
                  <li>
                    <a href="#" class="block py-2 px-4 hover:bg-gray-100 focus:bg-gray-100 outline-none">Another menu item</a>
                  </li>
                  <li>
                    <a href="#" class="block py-2 px-4 hover:bg-gray-100 focus:bg-gray-100 outline-none">Something else</a>
                  </li>
                </ul>
              </template>
            </Dropdown>
          </div>
        </div>
        <div>
          <div class="mt-4">
            <div class="mt-4">Using a list of buttons</div>
          </div>
          <div class="mt-4">
            <Dropdown class="inline" item-selector="li > button:not(.disabled):not(:disabled)" popper-class="w-64 bg-white border rounded-lg shadow-md">
              <!-- Dropdown trigger -->
              <button
                class="
                  dropdown-trigger
                  inline-block
                  px-6
                  py-3
                  bg-blue-600
                  text-white
                  leading-tight
                  rounded
                  hover:bg-blue-700
                  focus:bg-blue-700 focus:outline-none focus:ring-0
                  active:bg-blue-800
                  transition
                  duration-150
                  ease-in-out
                "
              >
                Dropdown button
              </button>
  
              <!-- Dropdown content -->
              <template #popper="{ hide }">
                <ul class="py-1 text-gray-70">
                  <li>
                    <button class="block py-2 w-full text-left px-4 hover:bg-gray-100 focus:bg-gray-100 outline-none" @click="hide">Click me to close</button>
                  </li>
                  <li>
                    <button class="block py-2 w-full text-left px-4 hover:bg-gray-100 focus:bg-gray-100 outline-none">Menu item</button>
                  </li>
                  <li>
                    <button class="block py-2 w-full text-left px-4 hover:bg-gray-100 focus:bg-gray-100 outline-none">Another menu item</button>
                  </li>
                  <li>
                    <button class="block py-2 w-full text-left px-4 hover:bg-gray-100 focus:bg-gray-100 outline-none">Something else</button>
                  </li>
                </ul>
              </template>
            </Dropdown>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import Dropdown from './Dropdown.vue';
  </script>
  
  <style scoped>
  .dropdown-trigger::after {
    display: inline-block;
    margin-left: 0.255em;
    vertical-align: 0.255em;
    content: '';
    border-top: 0.3em solid;
    border-right: 0.3em solid transparent;
    border-bottom: 0;
    border-left: 0.3em solid transparent;
  }
  </style>
  