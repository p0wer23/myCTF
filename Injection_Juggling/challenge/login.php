<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST["username"];
    $password = $_POST["password"];
    $passhash = hash('sha256', $password);

    $conn = mysqli_connect('db', 'php_docker', 'password', 'php_docker');
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    $sql = "SELECT id FROM users WHERE Role = ? and passhash = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("ss", $username, $passhash);
    $stmt->execute();
    $result = $stmt->get_result();

    if ($result->num_rows===1) {
        session_start();
        $_SESSION['Role'] = $username;
        header("Location: home.php");
        exit;
    } else {
        echo "Invalid username or password. Please try again.";
    }
}
?>
