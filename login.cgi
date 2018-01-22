#! /usr/bin/perl
use CGI;

print "Content-Type: text/html\n\n";
print '<!DOCTYPE html>
<html lang="hu">
    <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.3/css/bootstrap.min.css" integrity="sha384-Zug+QiDoJOrZ5t4lssLdxGhVrurbmBWopoEl+M6BdEfwnCJZtKxi1KgxUyJq13dy" crossorigin="anonymous">
        <title>Sunkari</title>
        <meta name="description" content="Sunkari finn-magyar online szótár">
        <meta name="author" content="Zsanett Ferenczi">
        <link rel="stylesheet" type="text/css" href="style.css">
        <link rel="stylesheet" href="font/css/font-awesome.min.css">
        <script>
        </script>
        <!--[if lt IE 9]>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7.3/html5shiv.js"></script>
        <![endif]-->
    </head>

    <body>
        <div class="container">
        <!--  NAVBAR  -->
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark mb-5">
            <a class="navbar-brand" href="index.cgi">Sunkari</a>
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>

                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav mr-auto">
                        <li class="nav-item active">
                            <a class="nav-link" href="index.cgi">Dictionary</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#"></a>
                        </li>
                    </ul>
                    <ul class="navbar-nav">
                        <a class="nav-link" href="#">Login</a>
                        <a class="nav-link" href="#">Register</a>

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
        <!-- END OF NAVBAR  -->
        <!-- LOGIN FORM  -->
        <div class="row">
            <div class="col-md-4 offset-4">
                <div class="text-center" style="padding:50px 0">
                    <div class="logo">login</div>
                        <!-- Main Form -->
                        <div class="login-form-1">
                            <form id="login-form" class="text-left">
                                <div class="login-form-main-message"></div>
                                <div class="main-login-form">
                                    <div class="login-group">
                                        <div class="form-group">
                                            <label for="lg_username" class="sr-only">Username</label>
                                                <input type="text" class="form-control" id="lg_username" name="lg_username" placeholder="username">
                                        </div>
                                        <div class="form-group">
                                            <label for="lg_password" class="sr-only">Password</label>
                                            <input type="password" class="form-control" id="lg_password" name="lg_password" placeholder="password">
                                       </div>
                                       <div class="form-group login-group-checkbox">
                                           <input type="checkbox" id="lg_remember" name="lg_remember">
                                           <label for="lg_remember">remember</label>
                                       </div>
                                   </div>
                                   <button type="submit" class="login-button"><i class="fa-ul fa fa-chevron-right"></i></button>
                               </div>
                               <div class="etc-login-form">
                                   <p>forgot your password? <a href="#">click here</a></p>
                                   <p>new user? <a href="#">create new account</a></p>
                               </div>
                            </form>
                        </div>
                        <!-- end:Main Form -->
                    </div>
                </div>
            </div>
        <!-- END OF LOGIN FORM -->
        </div>
    </div>
        
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.3/js/bootstrap.min.js" integrity="sha384-a5N7Y/aK3qNeh15eJKGWxsqtnX/wWdSZSKp+81YjTmS15nvnvxKHuzaWwXHDli+4" crossorigin="anonymous"></script>
    <script src="script.js"></script>
    </body>
</html>';

