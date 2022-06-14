<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Random Image Picker</title>
</head>
<body>
    <?php 
        $angka = rand(1,90);
        $angka = str_pad($angka, 2, '0', STR_PAD_LEFT);
        $file = "images/gambar_".$angka.".gif";
    ?>
    <p>Kotak anda :</p>
    <img src=<?php echo $file ?>>
    <br>
    <p>Susunan Kotak :</p>
    <p>1 2 3 ... 18</p>
    <p>.</p>
    <p>.</p>
    <p>.</p>
    <p>73 74 75 ...90</p>
</body>
</html>
