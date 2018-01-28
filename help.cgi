#! /usr/bin/perl
use CGI;

print "Content-Type: text/html\n\n";
print '<!DOCTYPE html>

<html lang="hu">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.3/css/bootstrap.min.css" integrity="sha384-Zug+QiDoJOrZ5t4lssLdxGhVrurbmBWopoEl+M6BdEfwnCJZtKxi1KgxUyJq13dy" crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="style.css">
    <link rel="stylesheet" href="font/css/font-awesome.min.css">
    <title>Sunkari</title>
    <meta name="description" content="Sunkari finn-magyar online szótár">
    <meta name="author" content="Zsanett Ferenczi">
    <script src="lib/marked.js"></script>
    <script>
        $(document).ready(function(){
            //sajat script
        });
    </script>
    <!--[if lt IE 9]>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7.3/html5shiv.js"></script>
    <![endif]-->
</head>


<!-- HA REGISZTRÁLT/LOGINOLT, akkor ne Login és Register gombok, hanem Edit és PROFIL gombok legyenek -->

<body>
    <div class="container">
        <!-- NAVBAR -->
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark mb-5">
            <a class="navbar-brand" href="index.cgi">Sunkari</a>
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
        <!-- BOTTOM  -->
        <div class="row mb-5">
            <!-- ENTRY LAYOUT  -->
            <div class="col-md-8 push-md-4 offset-md-1">
                <div class="row">
                    <div class="col-md-12">
                        <!-- markdown fileok? -->
                        <div id="content">
							<h2>Súgó</h2>
							<p>Leírása ennek</p>
							<div>
								<a name="bevezetes">Bevezetes</a>
								<p>Lorem ipsum dolor sit amet..Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.LoremLorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet. ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet...</p>
							</div>
							<div>
								<a name="vege">Vége</a>
								<p>Lorem ipsum dolor sit amet .Lorem ipsum dolor sit amet..Lorem ipsum dolor sit amet..Lorem ipsum dolor sit amet..Lorem ipsum dolor sit amet.<Lorem ipsum dolor sit amet./Lorem ipsum dolor sit amet.pLorem ipsum dolor sit ametLorem ipsum dolor sit ametLorem ipsum doLorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.lor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet...</p>
							</div>
						</div>
                        <!--<script>
                            document.getElementById("content").innerHTML =
							marked("### Sunkari - Finn-magyar-finn kétnyelvű online szótár");
                        </script>-->
                    </div>
                </div>

            </div><!-- end of entry layout -->
            <!-- TARTALOMJEGYZÉK -->
            <div class="col-md-3 order-md-first">
                <div class="btn-group-vertical btn-group-md btn-block">
                    <a href="#bevezetes" class="btn btn-outline-info">Első lépések</a>
                    <a href="#vege" class="btn btn-outline-info">A szótár használata</a>
                    <a href="phrases.cgi" class="btn btn-outline-info">Nincs a szótárban a szó, amit keresek</a>
                    <a href="freq.cgi" class="btn btn-outline-info">Gyakoriság <br class="rwd-break" style="display:none;"/>szerinti <br class="rwd-break" style="display:none;"/>rendezés</a>
                    <a href="proverbs.cgi" class="btn btn-outline-info">Szólások, <br class="rwd-break" style="display:none;"/>közmondások</a>
                </div>
            </div><!-- end of TARTALOMJEGYZÉK -->

        </div><!-- end of BOTTOM -->
    </div><!-- end of container -->
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.3/js/bootstrap.min.js" integrity="sha384-a5N7Y/aK3qNeh15eJKGWxsqtnX/wWdSZSKp+81YjTmS15nvnvxKHuzaWwXHDli+4" crossorigin="anonymous"></script>

    <script src="script.js"></script>
</body>
</html>';
