<?php

error_reporting(0);
function waf_check($input)
{
    $input=iconv('UTF-8', 'US-ASCII//TRANSLIT', $input);
    if(preg_match("/'/",$input))
    {
        return true;
    }
    else
    {
        return false;
    }
}


function send_to_api($data)
{
    $api_url = 'http://127.0.0.1:5000/login';
    $options = [
        'http' => [
            'method' => 'POST',
            'header' => 'Content-Type: application/x-www-form-urlencoded',
            'content' => $data,
        ],
    ];
    $context = stream_context_create($options);
    $result = file_get_contents($api_url, false, $context);
    
    if ($result !== false) 
    {
        echo "Response from Flask app: $result";
    } 
    else 
    {
        echo "Failed to communicate with Flask app.";
    }
}

if($_SERVER['REQUEST_METHOD'] === 'POST')
{
	if(!empty($_POST['username'])&&!empty($_POST['password']))
	{
        $username=$_POST['username'];
        if(waf_check($username) && $_SERVER['REMOTE_ADDR']!=="127.0.0.1")
        {
            die("WAF blocked");
        }
        else
        {
            send_to_api(file_get_contents("php://input"));
        }

	}
	else
	{
		echo "<script>alert('Please Fill All Fields')</script>";
	}
}




?>


<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Data Selection</title>
    </head>

    <body>
        <h2>    
            Data Selection
        </h2>
        <form method="POST">
            <div>
                <span></span>
                <input type="text" name="username" id="userName" placeholder="Username">
            </div>
            <div>
                <span></span>
                <input type="password" name="password" id="pwd" placeholder="Password">
            </div>
            <button>Login</button>
        </form>
    </body>
</html>