function selectdist() {
    var e = document.getElementById("stroke");
    var value = e.value;
    if(value == "fly" || value == "back" || value == "breast")
    {
        var ele = document.getElementsByName("distance");
        for(var i=0;i<ele.length;i++)
            ele[i].checked = false;
        document.getElementById('100l').style.display = 'block';
        document.getElementById('200l').style.display = 'block';
        document.getElementById('400l').style.display = 'none';
        document.getElementById('800l').style.display = 'none';
        document.getElementById('1500l').style.display = 'none';
    }
    else if(value == "free")
    {   
        var ele = document.getElementsByName("distance");
        for(var i=0;i<ele.length;i++)
            ele[i].checked = false; 
        document.getElementById('100l').style.display = 'block';
        document.getElementById('200l').style.display = 'block';
        document.getElementById('400l').style.display = 'block';
        document.getElementById('800l').style.display = 'block';
        document.getElementById('1500l').style.display = 'block';
    }
    else if(value == "im")
    {
        var ele = document.getElementsByName("distance");
        for(var i=0;i<ele.length;i++)
            ele[i].checked = false;
        document.getElementById('100l').style.display = 'none';
        document.getElementById('200l').style.display = 'block';
        document.getElementById('400l').style.display = 'block';
        document.getElementById('800l').style.display = 'none';
        document.getElementById('1500l').style.display = 'none';
    }
    else {
        var ele = document.getElementsByName("distance");
        for(var i=0;i<ele.length;i++)
            ele[i].checked = false;
        document.getElementById('100l').style.display = 'block';
        document.getElementById('200l').style.display = 'block';
        document.getElementById('400l').style.display = 'block';
        document.getElementById('800l').style.display = 'block';
        document.getElementById('1500l').style.display = 'block';
    }
    enableSubmit();
  }
  
  function validatefilledIn() {
    console.log('Form Submitted');
  }
  
  function enableSubmit() {
    let inputs = document.getElementsByClassName('required');
    let btn = document.querySelector('button[type="submit"]');
    let isValid = true;
    for (var i = 0; i < inputs.length; i++) {
      let changedInput = inputs[i];
      if (changedInput.value.trim() === "" || changedInput.value === null || ($('input[type=radio]:checked').size() === 0)) {
        isValid = false;
        break;
      }
    }
    btn.disabled = !isValid;
  }