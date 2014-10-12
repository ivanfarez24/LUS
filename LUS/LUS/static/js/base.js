/**
 * Created by Ivancho on 12/10/2014.
 */
$(function()
{
    $(".dropdown").click(function(e){
        var a = $(this).find("a");
        var href = $(a).attr("href");
        if (href)
            window.location.href = href;
    });
});
