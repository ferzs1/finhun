<?php
session_start();
?>


<!DOCTYPE html>

<html lang="hu">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.3/css/bootstrap.min.css" integrity="sha384-Zug+QiDoJOrZ5t4lssLdxGhVrurbmBWopoEl+M6BdEfwnCJZtKxi1KgxUyJq13dy" crossorigin="anonymous">
    <link rel="stylesheet" href="font/css/font-awesome.min.css">
    <link rel="stylesheet" type="text/css" href="style.css">
    <title>Sunkari</title>
    <meta name="description" content="Sunkari finn-magyar online szótár">
    <meta name="author" content="Zsanett Ferenczi">
	<meta http-equiv="Content-Type" content="text/html;charset=utf-8">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
  	<script src="https://code.jquery.com/jquery-1.10.2.js"></script>
    <!--[if lt IE 9]>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7.3/html5shiv.js"></script>
    <![endif]-->
</head>


<!-- HA REGISZTRÁLT/LOGINOLT, akkor ne Login és Register gombok, hanem Edit és PROFIL gombok legyenek -->

<body>
    <div class="container">
        <!-- NAVBAR -->
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark mb-5">
            <a class="navbar-brand" href="#">Sunkari</a>
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>


                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav mr-auto">
                        <li class="nav-item active">
                            <a class="nav-link" href="index.cgi">Szótár</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#"></a>
                        </li>
                    </ul>
                    <ul class="navbar-nav">
                        <a class="nav-link" href="login.cgi">Belépés</a>
                        <a class="nav-link" href="register.cgi">Regisztráció</a>
                        <a class="nav-link" href="help.cgi">Súgó</a>

						<li class="dropdown">
							<a class="nav-link dropdown-toggle" href="index.html" data-toggle="dropdown"><img src="hu.png" /><span class="pl-2">magyar</span>
						        <span class="caret"></span></a>
        					<ul class="dropdown-menu">
								<li class="dark-link"><a href="fi_index.html"><img src="fi.png" /><span class="pl-2">suomi</span></a></li>
        					</ul>
      					</li>
                    </ul>
                </div>
        </nav>
        <!-- SEARCH BAR  -->
        <div class="row mb-5">
            <div class="col-md-9">
                <div class="offset-md-4 offset-lg-4 offset-xl-4 offset-sm-2 col-md-8 col-lg-8 col-xl-8 col-xs-2 col-sm-8">
                    <form class="form" method="post" id="form" action="cgi-bin/search_form.php">
                        <div class="input-group">
                           <input type="text" class="form-control" name="word" id="word_search">
                           <span class="input-group-btn pl-1">
                                <input class="btn btn-outline-danger" type="submit" name="submit" value="Submit" id="btnbtn">
                           </span>
                        </div>
                    </form>
                </div>
            </div>
        </div> <!-- search bar vége -->
        <!-- BOTTOM  -->
        <div class="row mb-5">
            <!-- ENTRY LAYOUT  -->
            <div class="col-md-8 push-md-4 offset-md-1" id="content">
              <?php if($_SESSION['info']['success'] == true)
              {
                  echo '
                    <div class="row">
                      <div class="col-md-12">
                        <h2 class="text-uppercase"><strong>'. substr($_SESSION['info']['word'], 0, 1) .'<span style="font-size:18pt;">' . substr($_SESSION['info']['word'], 1) . '</span></strong></h2>
                      </div>
                    </div>
                    <div class="row">
                        <div class="col-md-12">
                            <p class="text-hidden">';
                    echo  $_SESSION['info']['pos'] . ', ' . $_SESSION['info']['cat'];
                   echo '</p>
                        </div>
                        </div>';
                // FOR LOOP
                  echo '
                    <div class="meaning">
                        <div class="row">
                            <div class="col-md-12">
                                <ul class="fa-ul">
                                    <li><i class="fa-li fa fa-angle-right"></i>kutya, eb</li>
                                </ul>
                                <div class="card border-info mb-4 offset-1">
                                    <div class="card-header border-info bg-info text-white">
                                        <h6 class="card-title mb-0 pb-0">Példamondat finnül hosszabban</h6>
                                    </div>
                                    <div class="card-body">
                                        <p class="card-text">Példamondat magyarul hosszabban</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                      </div> <!-- div meaning end -->';

              }
            //session_destroy();
            unset($_SESSION['info']);
          ?>
			</div>
            <!-- GOMBOK -->
            <div class="col-md-3 order-md-first">
                <div class="wod">
					<h3 class="text-center">A nap szava</h3>
					<a href="" id="under">Koira</a>
					<p><i class="fa fa-star"></i> meaning of the word, etc</p>
                </div>
				<p class="text-center">Rendezés</p>
				<div class="btn-group-vertical btn-group-md btn-block mb-5">
					<a href="tables.cgi" class="btn btn-outline-info">Témakörök <br class="rwd-break" style="display:none;"/>szerint</a>
					<a href="freq.cgi" class="btn btn-outline-info">Gyakoriság <br class="rwd-break" style="display:none;"/>szerint</a>
					<a href="phrases.cgi" class="btn btn-outline-info">Frázisok</a>
					<a href="proverbs.cgi" class="btn btn-outline-info">Szólások, <br class="rwd-break" style="display:none;"/>közmondások</a>
					<a href="words.cgi" class="btn btn-outline-info">Összes szó</a>
				</div>
			</div><!-- end of GOMBOK -->
		</div><!-- end of BOTTOM -->
    </div><!-- end of container -->
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.3/js/bootstrap.min.js" integrity="sha384-a5N7Y/aK3qNeh15eJKGWxsqtnX/wWdSZSKp+81YjTmS15nvnvxKHuzaWwXHDli+4" crossorigin="anonymous"></script>

    <script src="script.js"></script>
</body>
</html>
