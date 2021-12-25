function cartitem_validate()
{
    console.log('function called');
    var cartitems=document.getElementById("quantity");
    if(cartitems.value=="")
    {
        alert('No product added in cart');
        return false;
    }
    else
    {
        return true;
    }
}

function order_validate()
{
    var contact1=document.getElementById("contact1");
    var contact2=document.getElementById("contact2");
    var location=document.getElementById("location");

    if(contact1.value=="" || contact2.value=="" || location.value=="")
    {
        alert('Please fill out all the fields');
        return false;
    }
    else{
        return true;
    }

}

function signup_validate()
{
    var fname=document.getElementById("fname");
    var lname=document.getElementById("lname");
    var username=document.getElementById("username");
    var email=document.getElementById("email");
    var password=document.getElementById("password");
    var cpassword=document.getElementById("cpassword");
    
    if(fname=="" || lname=="" || username=="" || email=="" || password=="" || cpassword=="")
    {
        alert('Please fill out all the fields')
        return false;
    }
    else{
        return true;
    }





}