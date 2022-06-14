<?php

if(isset($_GET['submit'])){
    $email = $_GET['email'];
    $comment = $_GET['comment'];
    $admin = $_GET['admin'];

    setcookie("admin", "false", time() + 30);
    
    header("Location: ./process2.php?email=".$email."&comment=".$comment."&admin=".$admin);
}

?>