module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

    course: {
      app: 'course',
      sassDir: [
        '<%= course.app %>/sass'
      ],
      jsDir: [
        '<%= course.app %>/js'
      ],
      buildcss: [
        '<%= course.app %>/static/course/css'
      ],
      buildjs: [
        '<%= course.app %>/static/'
      ]
    },
    sass: {
          dev: {
            files: {
              '<%= course.buildcss %>/main.css': '<%= course.sassDir %>/main.scss',
              '<%= course.buildcss %>/pygments.css': '<%= course.sassDir %>/pygments.scss'
            }
          },
    },
    copy: {
       dev: {
              expand: true,
              src: ['<%= course.jsDir %>/**'],
              dest: '<%= course.buildjs %>/',
            },   
    },
    // concat: {
    //         dev: {
    //           src: ['<%= course.jsDir %>/**'],
    //           dest: '<%= course.buildjs %>/app.min.js',
    //         },
    // }, 
    watch: {
            options: {livereload: true},
            sass: {
                files: ['<%= course.sassDir %>/**'],
                tasks: ['sass']
            },
            // javascript: {
            //     files: ['<%= course.jsDir %>/**'],
            //     tasks: ['concat:dev']
            // }
            javascript: {
                files: ['<%= course.jsDir %>/**'],
                tasks: ['copy:dev']
            }
            // sass: {
            //     files: ['<%= course.sassDir %>'],
            //     tasks: ['sass']
            // }
    },
    // Task configuration goes here.

  });

  // Load plugins here.
  // grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-copy');
  // grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-sass');
  grunt.loadNpmTasks('grunt-contrib-watch');

  // Register tasks here.
  grunt.registerTask('default', ['sass', 'copy']);

};