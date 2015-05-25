module.exports = function (grunt) {
    require('load-grunt-tasks')(grunt);
    require('time-grunt')(grunt);

    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        clean: ['static/'],

        sass: {
            options: {
                includePaths: ['bower_components/foundation/scss'],
                outputStyle: 'compressed'
            },
            flop: {
                files: [{
                    'static/css/flop.min.css': 'flop/dashboard/static_src/scss/dashboard.scss'
                }]
            }
        },
        uglify: {
            options: {
                preserveComments: 'some'
                /*, // for debug
                 compress: false,
                 mangle: false,
                 beautify:true*/
            },
            flop: {
                files: [
                    {'static/js/flop.min.js': ['flop/dashboard/static_src/js/flop.js']},
                    {'static/js/modernizr.js': ['bower_components/modernizr/modernizr.js']},
                    {'static/js/placeholder.js': ['bower_components/jquery-placeholder/jquery.placeholder.js']},
                    {'static/js/fastclick.js': ['bower_components/fastclick/lib/fastclick.js']}
                ]
            }
        },

        copy: {
            flop: {
                files: [
                    {
                        nonull: true,
                        src: 'bower_components/jquery/dist/jquery.min.js',
                        dest: 'static/js/jquery.min.js'
                    }, {
                        nonull: true,
                        src: 'bower_components/foundation/js/foundation.min.js',
                        dest: 'static/js/foundation.min.js'
                    }, {
                        nonull: true,
                        src: 'bower_components/foundation/css/normalize.css',
                        dest: 'static/css/normalize.css'
                    }
                ]
            }
        },

        autoprefixer: {
            flop: {
                src: 'static/css/flop.min.css'
            }
        },

        newer: {
            options: {
                override: function (detail, include) {
                    if (detail.task === 'sass' && detail.path === 'flop/dashboard/static_src/css/flop.scss') {
                        include(true);
                    } else {
                        include(false);
                    }
                }
            }
        },
        //
        watch: {
            grunt: {files: ['Gruntfile.js']},
            options: {livereload: true},
            flop: {
                files: 'static_src/**/*.*',
                tasks: [
                    'newer:sass:flop', 'newer:uglify:flop', 'newer:copy:flop',
                    'newer:autoprefixer:flop'
                ]
            }
        }
    });

    grunt.registerTask('build', [
        'newer:sass', 'newer:uglify', 'newer:copy', 'newer:autoprefixer']);
    grunt.registerTask('default', ['build', 'watch']);
};
