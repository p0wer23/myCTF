<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST["username"];
    $password = $_POST["password"];
    $passhash = hash('sha256', $password);

    $conn = mysqli_connect('db', 'php_docker', 'password', 'php_docker');
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    $sql = "SELECT passhash FROM users WHERE Role = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("s", $username);
    $stmt->execute();
    $result = $stmt->get_result();

    if ($result->num_rows===1) {
        $row = $result->fetch_assoc();
        if ($row['passhash']==$passhash){
            session_start();
            $_SESSION['Role'] = $username;
            header("Location: home.php");
            exit;
        }
        echo "Wrong password";
        exit;
    } else {
        echo "Invalid username. Please try again.";
    }
}
?>