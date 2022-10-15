// 2. Lenght converter
function converter(ft) {
    const results = {
     meters: ft * 0.3048,
     cm: ft * 30.48,
     inches: ft * 12,
     yard: ft * 0.333,
    };
   
    return results;
   }
   
   console.log(converter(6));