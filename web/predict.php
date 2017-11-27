<?php 

echo $_POST['inputUrl'];

$url_string = $_POST['inputUrl'];
$limit = 10;

$url = 'http://localhost:5000/svm';
$data = array('url' => $url_string, 'scrape_limit' => $limit);

// use key 'http' even if you send the request to https://...
$options = array(
    'http' => array(
        'header'  => "Content-type: application/x-www-form-urlencoded\r\n",
        'method'  => 'POST',
        'content' => http_build_query($data)
    )
);

$context  = stream_context_create($options);
$result = file_get_contents($url, false, $context);
if ($result === FALSE) { /* Handle error */ }

$response = array('score' => $result)
header('Access-Control-Allow-Origin: *');
var_dump($response);
var_dump(http_response_code(404));

// header("Location: index.php#about?score=".$result);

?>