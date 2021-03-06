<!DOCTYPE html>

<html lang="en">

<script>
function showScore(url, limit) {
  console.log(url)
  document.getElementById("score").innerHTML = "Getting reviews . . .";
  var xmlhttp = new XMLHttpRequest();
  xmlhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
          document.getElementById("score").innerHTML = this.responseText;
      }
  };
  xmlhttp.open("POST", "http://localhost:5000/svm", true);
  xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xmlhttp.send("url=" + url + "&scrape_limit=" + limit);
}
</script>

  <head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>IMDb Score Approximation</title>

    <!-- Bootstrap Core CSS -->
    <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom Fonts -->
    <link href="vendor/font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css">
    <link href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,700,300italic,400italic,700italic" rel="stylesheet" type="text/css">

    <!-- Custom CSS -->
    <link href="css/stylish-portfolio.css" rel="stylesheet">

  </head>

  <body>
    <!-- Navigation -->
    <a id="menu-toggle" href="#" class="btn btn-dark btn-lg toggle">
      <i class="fa fa-bars"></i>
    </a>
    <nav id="sidebar-wrapper">
      <ul class="sidebar-nav">
        <a id="menu-close" href="#" class="btn btn-light btn-lg pull-right toggle">
          <i class="fa fa-times"></i>
        </a>
        <li class="sidebar-brand">
          <a class="js-scroll-trigger" href="#top">Start Bootstrap</a>
        </li>
        <li>
          <a class="js-scroll-trigger" href="#top">Home</a>
        </li>
        <li>
          <a class="js-scroll-trigger" href="#about">About</a>
        </li>
        <li>
          <a class="js-scroll-trigger" href="#services">Services</a>
        </li>
        <li>
          <a class="js-scroll-trigger" href="#portfolio">Portfolio</a>
        </li>
        <li>
          <a class="js-scroll-trigger" href="#contact" onclick=$( "#menu-close").click();>Contact</a>
        </li>
      </ul>
    </nav>

    <!-- Header -->
    <header class="header" id="top">
      <div class="text-vertical-center">
        <h1>Sentiment Analysis Movie IMDB</h1>
        <h3>Alson Cahyadi - 13514035</h3>
        <h3>Ramos Janoah - 13514089</h3>
        <h3>Jovian Christianto - 13514101</h3>
        <a href="#about" class="btn btn-dark btn-lg js-scroll-trigger">Go to App</a>
      </div>
    </header>

    <!-- About -->
    <section id="about" class="header">
      <div class="container text-center">
        <br>
        <br>
        <h1>Predict Score Movie</h1>
        <form action="predict.php" method="POST"> 
            <br>
            <br>
          <h2>Movie Review URL</h2>
          <textarea id="url" class="input" rows="1" cols="40" placeholder="Movie review url here ..." name="inputUrl"></textarea>
          <br>
          <p>
          <h2>Scrape Limit</h2>
          <input type="number" style="width:10%; margin:1em" value="100" placeholder="Scrape limit" id="scrape_limit">
          <br>
          <br>
          <input type="button" style="width:20%;" value="Predict" onclick="
          showScore(
            document.getElementById('url').value,
            document.getElementById('scrape_limit').value,
          )
          ">
        </form> 
        <br>
        <h2>Score :
          <p id='score'>
          </p> 
        </h2>`
      </div>
      <!-- /.container -->
    </section>

    <!-- Footer -->
    <!-- <footer>
      <div class="container">
        <div class="row">
          <div class="col-lg-10 mx-auto text-center">
            <h4>
              <strong>Start Bootstrap</strong>
            </h4>
            <p>3481 Melrose Place
              <br>Beverly Hills, CA 90210</p>
            <ul class="list-unstyled">
              <li>
                <i class="fa fa-phone fa-fw"></i>
                (123) 456-7890</li>
              <li>
                <i class="fa fa-envelope-o fa-fw"></i>
                <a href="mailto:name@example.com">name@example.com</a>
              </li>
            </ul>
            <br>
            <ul class="list-inline">
              <li class="list-inline-item">
                <a href="#">
                  <i class="fa fa-facebook fa-fw fa-3x"></i>
                </a>
              </li>
              <li class="list-inline-item">
                <a href="#">
                  <i class="fa fa-twitter fa-fw fa-3x"></i>
                </a>
              </li>
              <li class="list-inline-item">
                <a href="#">
                  <i class="fa fa-dribbble fa-fw fa-3x"></i>
                </a>
              </li>
            </ul>
            <hr class="small">
            <p class="text-muted">Copyright &copy; Your Website 2017</p>
          </div>
        </div>
      </div>
      <a id="to-top" href="#top" class="btn btn-dark btn-lg js-scroll-trigger">
        <i class="fa fa-chevron-up fa-fw fa-1x"></i>
      </a>
    </footer> -->

    <!-- Bootstrap core JavaScript -->
    <script src="vendor/jquery/jquery.min.js"></script>
    <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

    <!-- Plugin JavaScript -->
    <script src="vendor/jquery-easing/jquery.easing.min.js"></script>

    <!-- Custom scripts for this template -->
    <script src="js/stylish-portfolio.js"></script>

  </body>

</html>
