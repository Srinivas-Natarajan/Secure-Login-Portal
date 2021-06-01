var express = require('express');
var bodyParser = require('body-parser');
var app = express();
var async = require('async');
var path = require('path')


app.use(express.static("public"));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.set("views", "./views");
app.set("view engine", "ejs");

app.use(express.static(__dirname + '/public'));


app.get("/", (req, res) => {
  /*
  var spawnSync = require("child_process").spawnSync
  var process = spawnSync('D:/Anaconda/envs/ISM/python',["./ml/preload.py"])  
  
  var er = process.stderr.toString()
  if (er) { console.log(er)}
  result = process.stdout.toString().trim()
  console.log("Loading: \n", result)
  */
  res.sendFile(__dirname + "/views/index.html");
});


app.get('/form', function(req, res){

  var email = req.query.inputEmail
  var pwd = req.query.inputPassword

  console.log("Email: ",email);
  console.log("Password: ",pwd);

  var spawnSync = require("child_process").spawnSync
  var process = spawnSync('D:/Anaconda/envs/ISM/python',["./ml/prediction.py",email,pwd])  
  
  var er = process.stderr.toString()
  if (er) { console.log(er)}

  result = process.stdout.toString().trim()
  console.log("Result: ", result)
  console.log(typeof result)
  if(result.includes("0.0"))
    res.sendFile(__dirname + "/views/success.html");
  else  
  res.sendFile(__dirname + "/views/fail.html");
});

app.listen(3000, function() { //Set port to listen to
  console.log('Server running at http://127.0.0.1:3000/');
  });
