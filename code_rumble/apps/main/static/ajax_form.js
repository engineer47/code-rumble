// AJAX for posting
function create_post() {
    console.log("create post is working!") // sanity check
    var job_type = "";
    $("my_jobs").on( "click", "tr", function() {
  		//job_type="my_job";
  		alert("good");
	});
	
    $("available_jobs").on( "click", "tr", function() {
  		//var job_type = "available_jobs";
  		alert("bad");
	});
    $.ajax({
        url : "job_url", // the endpoint
        type : "GET", // http method
        data : { job_type : job_type }, // data sent with the post request

        // handle a successful response
        //success : function(json) {
        //    $('#post-text').val(''); // remove the value from the input
        //    console.log(json); // log the returned json to the console
        //    console.log("success"); // another sanity check
        //},

        // handle a non-successful response
        //error : function(xhr,errmsg,err) {
        //    $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
        //        " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
        //    console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        //}
    });
};