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
        <!-- SEARCH BAR  -->
        <div class="row mb-5">
            <div class="col-md-9">
                <div class="offset-md-4 offset-lg-4 offset-xl-4 offset-sm-2 col-md-8 col-lg-8 col-xl-8 col-xs-2 col-sm-8">
                    <form class="form" action="">
                        <div class="input-group">
                           <input type="text" class="form-control">
                           <span class="input-group-btn pl-1">
                                <button class="btn btn-outline-danger" type="button">Keres</button>
                           </span>
                        </div>
                    </form>
                </div>
            </div>
        </div> <!-- search bar vége -->
        <!-- BOTTOM  -->
        <div class="row mb-5">
            <!-- ENTRY LAYOUT  -->
            <div class="col-md-8 push-md-4 offset-md-1">
                <div class="row">
                    <div class="col-md-12">
						<!-- csak egy betű lesz nagy, a többi 18-as-->
						<h2 class="text-uppercase"><strong>S<span style="font-size:18pt;">úgó</span></strong></h2>
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-12">
                        <!-- markdown fileok? -->
                        <div id="content"></div>
                        <script>
                            document.getElementById("content").innerHTML =
                                  marked("* render \n* render 2\n* render 3");
                        </script>
                    </div>
                </div>

            </div><!-- end of entry layout -->
            <!-- TARTALOMJEGYZÉK -->
            <div class="col-md-3 order-md-first">
                <div class="btn-group-vertical btn-group-md btn-block">
                    <a href="tables.cgi" class="btn btn-outline-info">Táblázatok</a>
                    <a href="words.cgi" class="btn btn-outline-info">Összes szó</a>
                    <a href="phrases.cgi" class="btn btn-outline-info">Frázisok</a>
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
