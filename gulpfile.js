var gulp = require('gulp');
var uglifycss = require('gulp-uglifycss');

gulp.task('css', function(){
    gulp.src('./blog/static/css/blog.css')
        .pipe(uglifycss({}))
        .pipe(gulp.dest('./blog/static/build'));
});

gulp.task('default', ['css']);
