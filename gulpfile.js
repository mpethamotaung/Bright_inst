const gulp = require('gulp');
const concat = require('gulp-concat');
const cleanCSS = require('gulp-clean-css');

gulp.task('css', function() {
    return gulp.src([
        'tut_platform/assets/css/Cookie.css',
        'tut_platform/assets/css/Noto%20Sans%20Syriac%20Eastern.css',
        'tut_platform/assets/css/Availability---Manage-availability-bookings-appointments_v1.css',
        'tut_platform/assets/css/Documents-App-Browser.css',
        'tut_platform/assets/css/Hero-Clean-Reverse-images.css',
        'tut_platform/assets/css/Navbar-Centered-Links-icons.css',
        'tut_platform/assets/css/Pretty-Footer-.css',
        'tut_platform/assets/css/Pricing-Free-Paid-badges.css',
        'tut_platform/assets/css/Profile-Edit-Form-styles.css',
        'tut_platform/assets/css/Profile-Edit-Form.css',
        'tut_platform/assets/css/Profile-with-data-and-skills.css',
        'tut_platform/assets/css/Staff-Directory.css',
        'tut_platform/assets/css/Testimonials-BS5.css'
    ])
    .pipe(concat('combined.min.css'))
    .pipe(cleanCSS())
    .pipe(gulp.dest('assets/css'))
    .on('error', function(err) {
        console.error('Error in css task', err.toString());
    });
});

gulp.task('default', gulp.series('css'));
