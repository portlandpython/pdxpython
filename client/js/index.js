var Mustache = require('mustache');
var $ = require('jquery');
var moment = require('moment');

$.getJSON('/meetup_calendar', function(data) {
  var wrapTime = function() {
    return function(text, render) {
      return moment(parseInt(render(text), 10)).format("dddd, MMMM Do");
    }
  }
  var template = $('#calendarTemplate').html();
  var output = Mustache.render(template, {events: data, date: wrapTime});
  $('#calendar').html(output);
});
