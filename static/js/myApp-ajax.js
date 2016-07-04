$('#likes').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/myApp/like_category/', {category_id: catid}, function(data){
               $('#like_count').html(data);
               $('#likes').hide();
    });
});


$('#suggestion').keyup(function(){
        var query;
        query = $(this).val();
        $.get('/myApp/suggest_category/', {suggestion: query}, function(data){
         $('#cats').html(data);
        });
});
