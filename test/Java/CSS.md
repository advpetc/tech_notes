```css
@CHARSET "UTF-8";

html{
 height:100%;
}
hr {
 margin-right:10px;
 margin-left:10px;
 height: 2px;
 background: url(http://ibrahimjabbari.com/english/images/hr-11.png) repeat-x 0 0;
    border-top: 1px dashed #866760;
}
table{
 border-radius:10px;
 border-collapse: collapse;
}
th {
    background-color: #7c7dca;
    color: white;
    border-bottom:2px dashed white;
}

input[type=text]:focus {
    background-color: #d9e6e5;
}
input[type=text]:hover {
    width:170px;
}
input[type=text] {
    width: 200px;
    box-sizing:border-box;
    border: 2px solid #ccc;
    border-radius: 4px;
    font-size: 16px;
    padding: 5px 5px 5px 10px;
    -webkit-transition: width 0.4s ease-in-out;
    transition: width 0.4s ease-in-out; 
}

body{
 background-image: linear-gradient(to bottom, rgba(33,97,140,0.3) 0%,rgba(213,219,219,0.3) 100%);
 width: 100%;
 background-repeat: no-repeat;
 background-size: cover;
 background-attachment: fixed;
}
th{
 font-family: 'Macondo', Cursive;
}
a:hover{
 background-color: rgba(230,230,230,0.6);
}
a{
 text-decoration: none;
 color:#5f609a;
}
#leftTd{
 position:fixed;
}

input{
 animation:showInput 3s ease 1 forwards;
}

#centerTd{
 animation:showTable 1s ease 1 forwards;
 margin-bottom:100px;
}

#uscImage{
 -webkit-animation:spin 8s linear infinite;
    -moz-animation:spin 8s linear infinite;
 animation:spin 8s linear infinite;
}


@keyframes spin { 100% { -webkit-transform: rotate(360deg); transform:rotate(360deg); } }
@-moz-keyframes spin { 100% { -moz-transform: rotate(360deg); } }
@-webkit-keyframes spin { 100% { -webkit-transform: rotate(360deg); } } 

@-webkit-keyframes showInput{
   0%{
    opacity: 0;
    width: 100px;
    
   }
   50%{
    opacity: 0.5;
    width: 90px;

   }
   100%{
    opacity: 1;
    width: 100px;
    
   }
  }

@-webkit-keyframes showTable{
   0%{
    opacity: 0;
   }
   50%{
    opacity: 0.5;
   }
   100%{
    opacity: 1;
   }
  }
```