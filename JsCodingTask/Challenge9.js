// Task_9

// Return the number of vowels in a string


function vowel_count(str1)
{
  let vowel_list = 'aeiouAEIOU';
  let vstring = 0;
  
  for(let i = 0; i < str1.length ; i++)
  {
    if (vowel_list.indexOf(str1[i]) !== -1)
    {
      vstring += 1;
    }
  
  }
  return vstring;
}
console.log(vowel_count("HENRY aND PeaCE"));