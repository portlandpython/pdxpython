module.exports = function(grunt) {

  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    browserify: {
      dist: {
        files: {
          'pdxpython/static/module.js': ['javascript/**/*.js']
        }
      }
    },
    less: {
      development: {
        options: {
          paths: ['client-side/less']
        },
        files: {
          'pdxpython/static/style.css': 'client-side/style.less'
        }
      }
    }
  });

  grunt.loadNpmTasks('grunt-browserify');
  grunt.loadNpmTasks('grunt-contrib-less');

  grunt.registerTask('default', ['browserify', 'less']);
}
