<?php
session_start();

if (isset($_SESSION['Role'])) {
    
} else {
    header("Location: login.php");
    exit();
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Login Page</title>
</head>
<body>

<h3>Search Roles:</h3>

<form action="home.php" method="GET">
    <label for="Search">Role:</label>
    <input type="text" name="Search" id="username" required><br><br>
    <input type="submit" value="Search">
</form>

<hr>

<?php

if (isset($_GET["Search"])){
    $search = $_GET["Search"];
    $connect = mysqli_connect('db', 'php_docker', 'password', 'php_docker');
    $table_name = "users";
    $query = "SELECT id, Role from $table_name where Role='$search'";
    $response = mysqli_query($connect, $query);

    echo "<strong>Roles:</strong>";
    while ($i = mysqli_fetch_assoc($response))
    {
        echo "<p>".$i['id'].". ";
        echo $i['Role']."</p>";
    }
}
?>

</body>
</html>

<?php
if ($_SESSION['Role']==='Head')
    echo "flag"

?>