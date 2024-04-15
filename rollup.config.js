import { fileUrlToPath } from 'node:url';

export default {

    external: [
        'airfoilDataConvert',
        fileUrlToPath(
            new URL(
                '/src/utils/airfoilDataConvert.js',
                import.meta.url
            )
        ),
        /node_modules/
    ]
};