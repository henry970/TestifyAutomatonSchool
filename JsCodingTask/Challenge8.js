// Task_8
//  Return a Boolean if a number is divisible by 10

let boolean = function(number) {

    if (number % 10 !== 1) {
          return true;  
      }
      else {
          return false;    
      }
  };
  console.log(boolean(42))