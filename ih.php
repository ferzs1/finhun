<?php

session_start();

$word = $_POST['word'];


$servername = "localhost";
$username = "sunkarisql";
$password = "sqlJQ3Qd0";
$dbname = "sunkari_dict";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}


$sql = "SELECT * FROM Entry WHERE word LIKE '$word'";

$result = $conn->query($sql);
if (mysqli_num_rows($result) > 0) {
    while($row = $result->fetch_assoc()) {
        $info = "id: " . $row["ID"]. " word: " . $row["word"]. " category: " . $row["category"]. "<br>pos: " . $row['pos'];
        $_SESSION['info'] = $info;
    }
} else {
    echo "0 results";
    echo $word;
}

header('Location: ../index.php');
?>
