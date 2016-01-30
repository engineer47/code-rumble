
function submit_available_jobs() {

    console.log("create post is working!") // sanity check
  	$("#my_available_jobs_form").submit();

};

// AJAX for posting
function submit_my_jobs() {
  	$("#my_jobs_form").submit();

};

$(document).ready(function() {
 
    $('#job_table tbody').on( 'click', 'tr', function () {
        $(this).toggleClass('selected');
        $("tr:even").css("background-color", "white");
        $("tr:odd").css("background-color", "white");
        $(this).css("background-color", "#d3d3d3");
  
        var Something = $(this).closest('td').children('1').text();
        var vaaal = $(this).children().val();
        alert(vaaal);
    } );
 
   // $('#button').click( function () {
   //     alert( table.rows('.selected').data().length +' row(s) selected' );
    //} );
} );
