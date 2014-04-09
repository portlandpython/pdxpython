module.exports = function(grunt) {

  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    browserify: {
      dist: {
        files: {
          'pdxpython/static/module.js': ['client/js/**/*.js']
        }
      }
    },
    less: {
      development: {
        options: {
          paths: ['client/less']
        },
        files: {
          'pdxpython/static/style.css': 'client/less/main.less'
        }
      }
    }
  });

  grunt.loadNpmTasks('grunt-browserify');
  grunt.loadNpmTasks('grunt-contrib-less');

  grunt.registerTask('default', ['browserify', 'less']);
}
