var express = require("express");
var bodyParser = require('body-parser');
var app = express();

app.use(express.static("public"));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.set("views", "./views");
app.set("view engine", "ejs");



app.get("/", (req, res) => {

  var spawnSync = require("child_process").spawnSync
  var process = spawnSync('D:/Anaconda/envs/ISM/python',["./ml/preload.py"])  
  
  var er = process.stderr.toString()
  if (er) { console.log(er)}
  result = process.stdout.toString().trim()
  console.log("Loading: \n", result)

  res.sendFile(__dirname + "/views/index.html");
});


app.post('/', function(req, res){

  console.log(req.body.inputEmail);
  console.log(req.body.inputPassword);
  var spawnSync = require("child_process").spawnSync
  var process = spawnSync('D:/Anaconda/envs/ISM/python',["./ml/prediction.py",req.body.inputEmail,req.body.inputPassword])  
  
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

app.listen(3000);
