import createEmployeesObject from './11-createEmployeesObject.js';
import createReportObject from './12-createReportObject.js';

const employees = {
    ...createEmployeesObject('engineering', ['Bob', 'Jane']),
    ...createEmployeesObject('marketing', ['Sylvie'])
};      

const report = createReportObject(employees);
console.log(report.allEmployees);
console.log(report.getNumberOfDepartments(report.allEmployees));function Box(height, width) {
    this.height = height;
    this.width = width;
  }
  
  function Widget(height, width, color) {
    Box.call(this, height, width);
    this.color = color;
  }
  
  let widget = new Widget('red', 100, 200);
  
  console.log(widget);