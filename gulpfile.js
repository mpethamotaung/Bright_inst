const gulp = require('gulp');
const concat = require('gulp-concat');
const cleanCSS = require('gulp-clean-css');
const plumber = require('gulp-plumber');
const log = require('fancy-log');
const colors = require('ansi-colors');

gulp.task('css', function(done) {
    log('Starting CSS task...');
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
        'assets/css/Testimonials-BS5.css'
    ])
    .pipe(plumber({
        errorHandler: function(err) {
            log.error(colors.red('Error in CSS task'));
            log.error(colors.red(err.message));
            this.emit('end');
        }
    }))
    .pipe(concat('combined.min.css'))
    .pipe(cleanCSS())
    .pipe(gulp.dest('assets/css'))
    .on('end', function() {
        log('CSS task completed');
        done();
    });
});

gulp.task('default', gulp.series('css', function(done) {
    log('Default task started...');
    done();
}));
