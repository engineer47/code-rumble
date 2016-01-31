
function submit_available_jobs() {

    console.log("create post is working!") // sanity check
  	//$("#my_available_jobs_form").submit();

};

// AJAX for posting
function submit_my_jobs() {
  	//$("#my_jobs_form").submit();

};

$(document).ready(function() {
 
    $('#job_table tbody').on( 'click', 'tr', function () {
        $(this).toggleClass('selected');
        $("tr:even").css("background-color", "white");
        $("tr:odd").css("background-color", "white");
        $(this).css("background-color", "#d3d3d3");
        var index = $(this).index();
        var name = "#form" + index;
        alert(name);
        $(name).submit();
        $("#my_available_jobs_form").submit();
    } );
} );

$(function() {
	var index = 0
	$( "select" ).mouseover(function() {
  		index =$(this).parent().parent().index();
	});

 	$("select").on( 'click', function () {
 		
        var name = "#form" + index;
        var combo_val ="#job_status" + index;
        $(combo_val).val($(this).val());
        alert($(combo_val).val());
        //var elem_job_status = name +" #job_status"
        //alert(elem_job_status);
        //alert($(elem_job_status).val());
        //change_job_form = $(name);
        //alert(change_job_form.job_status);
                
        $(name).submit();
    });
});

