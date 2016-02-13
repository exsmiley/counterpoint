var express = require('express');
var app = express();

var mongoose = require('mongoose');

// application -------------------------------------------------------------
app.use(express.static('views'))
    
app.all('/*', function ( req, res ) {
        res.sendFile(__dirname + '/views/index.html');
})
app.on( 'error', function( error ){
       console.log( "Error: \n" + error.message );
       console.log( error.stack );
});

app.listen(3000);