<?php
$INN = $_POST['INN'];
$Name = $_POST['Name of organization'];
$Adress = $_POST['Adress'];
$Number = $_POST['Number of organization'];
$Supervisor = $_POST['Supervisor'];
$Shedule= $_POST['Shedule'];
$First = $_POST['First name'];
$Last = $_POST['Last name'];
$Patronymic = $_POST['Patronymic'];
$Date = $_POST['Date of employment'];
$Subdivision = $_POST['Subdivision'];
$Password = hash('sha256',$_POST['Password']);


// Параметры для подключения
$db_host = "localhost:3307";
$db_user = "root"; // Логин БД
$db_password = "root"; // Пароль БД
$db_base = 'diplom'; // Имя БД
$db_table = "diplom"; // Имя Таблицы БД

try {
    // Подключение к базе данных
    $db = new PDO("mysql:host=$db_host;dbname=$db_base", $db_user, $db_password);
    // Устанавливаем корректную кодировку
    $db->exec("set names utf8");
    // Собираем данные для запроса
    $data = array( 'INN' => $INN, 'Name of organization' => $Name, 'Adress' => $Adress, 'Number' => $Number, 'Supervisor' => $Supervisor, 'Shedule' => $Shedule, 'First name' => $First, 'Last name' => $Last, 'Patronymic' => $Patronymic, 'Date of employment' => $Date, 'Subdivision' => $Subdivision, 'Password' => $Password);
    // Подготавливаем SQL-запрос
    $query = $db->prepare("INSERT INTO $db_table (INN, Name, Adress, Number, Supervisor, Shedule, First, Last, Patronymic, Date, Subdivision, Password) values (:INN, :Name of organization, :Adress, :Number of organization, :Supervisor, :Shedule, :First name, :Last name, :Patronymic, :Date of employment, :Subdivision, :Password)");
    // Выполняем запрос с данными
    $query->execute($data);
    $result = true;
} catch (PDOException $e) {
    // Если есть ошибка соединения, выводим её
    print "Ошибка!: " . $e->getMessage() . "<br/>";
}

if ($result) {
  echo "Информация занесена в базу данных";
}

?>