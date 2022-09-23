<!doctype html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Redcrude Dashboard</title>
    <meta name="robots" content="index, follow" />
    <meta name="description" content="" />
    <meta name="keywords" content="" />
    <meta name="author" content="Gapconcepts" />
    <meta name="copyright" content="" />


    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <!-- data table -->
    <link rel="stylesheet" href="https://cdn.datatables.net/1.11.3/css/dataTables.bootstrap5.min.css">
    <link rel="stylesheet" href="https://cdn.datatables.net/responsive/2.2.9/css/responsive.bootstrap.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.13/css/select2.min.css">
    <!-- slider -->
    <link rel="stylesheet" href="https://unpkg.com/swiper@7/swiper-bundle.min.css" />

    <!-- compulsory global.css -->
    <link rel="stylesheet" href="main.css">
    <link rel="stylesheet" href="assets/sass/utility/typography.css">
    <link rel="stylesheet" href="assets/css/media.css">

    <!-- fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@100;200;300;400;500;600;700;800;900&display=swap" rel="stylesheet">


    <!-- icons -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.7.2/font/bootstrap-icons.css">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
</head>

<body>
    <!-- start side bar -->

    <div id="layoutSidenav">
        <div id="layoutSidenav_nav">
            <div class="logo d-none d-md-block">
                <img src="assets/images/logo.png" alt="">
            </div>
            <nav class="sb-sidenav accordion bg-white" id="sidenavAccordion">
                <div class="sb-sidenav-menu">
                    <div class="cover-nav">
                        <div class="nav">
                            <div class="sb-sidenav-menu-heading">Main Menu</div>

                            <a class="nav-link active" href="index.php">
                                <div class="sb-nav-link-icon"><img src="assets/images/icons/dashboard.svg" alt=""></div>
                                Dashboard
                            </a>

                            <a class="nav-link collapsed sidenav-active" href="#" data-bs-toggle="collapse" data-bs-target="#collapsePages" aria-expanded="false" aria-controls="collapsePages">
                                <div class="sb-nav-link-icon"><img src="assets/images/icons/courses.svg" alt=""></div>
                                Courses
                                <div class="sb-sidenav-collapse-arrow"><i class="fa fa-angle-down"></i></div>
                            </a>
                            <div class="collapse" id="collapsePages" aria-labelledby="headingTwo" data-bs-parent="#sidenavAccordion">

                                <nav class="sb-sidenav-menu-nested nav accordion" id="sidenavAccordionPages">
                                    <a class="nav-link" href="create-new-courses.php">
                                        <div class="sb-nav-link-icon"><img src="assets/images/icons/new-course.svg" alt=""></div>
                                        New Course
                                        <!-- <div class="sb-sidenav-collapse-arrow"><i class="fas fa-angle-down"></i></div> -->
                                    </a>
                                </nav>
                                <nav class="sb-sidenav-menu-nested nav accordion" id="sidenavAccordionPages">
                                    <a class="nav-link " href="#.">
                                        <div class="sb-nav-link-icon"><img src="assets/images/icons/courses.svg" alt=""></div>
                                        All Courses
                                        <!-- <div class="sb-sidenav-collapse-arrow"><i class="fas fa-angle-down"></i></div> -->
                                    </a>
                                </nav>
                            </div>

                            <a class="nav-link" href="explore-course.php">
                                <div class="sb-nav-link-icon"><img src="assets/images/icons/Explore-Courses.svg" alt="">
                                </div>
                                Explore Courses

                            </a>
                            <a class="nav-link" href="my-learning.php">
                                <div class="sb-nav-link-icon"><img src="assets/images/icons/My-Learning.svg" alt="">
                                </div>
                                My Learning
                            </a>
                            <a class="nav-link" href="expert-teacher.php">
                                <div class="sb-nav-link-icon"><img src="assets/images/icons/Expert-Teachers.svg" alt="">
                                </div>
                                Expert Teachers
                            </a>
                            <a class="nav-link" href="expert-trade.php">
                                <div class="sb-nav-link-icon"><img src="assets/images/icons/Expert-Traders.svg" alt="">
                                </div>
                                Expert Traders
                            </a>

                            <a class="nav-link" href="#.">
                                <div class="sb-nav-link-icon"><img src="assets/images/icons/Buy-&-Sell.svg" alt="">
                                </div>
                                Buy & Sell
                            </a>


                            <a class="nav-link" href="#.">
                                <div class="sb-nav-link-icon"><img src="assets/images/icons/Trading-Activity.svg" alt=""></div>
                                Trading Activity
                            </a>
                            <a class="nav-link" href="#.">
                                <div class="sb-nav-link-icon"><img src="assets/images/icons/market-capital.svg" alt=""></div>
                                Market Capital
                            </a>

                            <a class="nav-link" href="#.">
                                <div class="sb-nav-link-icon"><img src="assets/images/icons/Test.svg" alt=""></div>
                                Test
                            </a>

                            <a class="nav-link" href="#.">
                                <div class="sb-nav-link-icon"><img src="assets/images/icons/Certification.svg" alt="">
                                </div>
                                Certification
                            </a>
                            <a class="nav-link" href="#.">
                                <div class="sb-nav-link-icon"><img src="assets/images/icons/Wishlist.svg" alt=""></div>
                                Wishlist
                            </a>
                        </div>
                    </div>
                </div>

            </nav>
        </div>