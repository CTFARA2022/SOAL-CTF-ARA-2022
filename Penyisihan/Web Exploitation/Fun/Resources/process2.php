<?php

$email = $_GET['email'];
$comment = $_GET['comment'];
$admin = strtolower($_GET['admin']);
$admin_cookie = strtolower($_COOKIE['admin']);

if($admin == "true" && $admin_cookie == "true"){
    header("Location: ./files/asdqwdd.html");
}else{
    unset($_COOKIE['admin']);
    header("Location: ./goback.html");
}





?>