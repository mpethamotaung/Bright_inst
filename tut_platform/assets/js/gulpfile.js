const gulp = require('gulp');
const concat = require('gulp-concat');
const cleanCSS = require('gulp-clean-css');

gulp.task('css', function() {
    return gulp.src([
        'assets/css/Cookie.css',
        'assets/css/Noto%20Sans%20Syriac%20Eastern.css',
        'assets/css/Availability---Manage-availability-bookings-appointments_v1.css',
        'assets/css/Documents-App-Browser.css',
        'assets/css/Hero-Clean-Reverse-images.css',
        'assets/css/Navbar-Centered-Links-icons.css',
        'assets/css/Pretty-Footer-.css',
        'assets/css/Pricing-Free-Paid-badges.css',
        'assets/css/Profile-Edit-Form-styles.css',
        'assets/css/Profile-Edit-Form.css',
        'assets/css/Profile-with-data-and-skills.css',
        'assets/css/Staff-Directory.css',
        'assets/css/Testimonials-BS5.css',
        // Add other CSS files here
    ])
    .pipe(concat('combined.min.css'))
    .pipe(cleanCSS())
    .pipe(gulp.dest('assets/css'));
});

gulp.task('default', gulp.series('css'));
