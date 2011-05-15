<%inherit file="/base.mako" />

<%def name="head_tags()">

	<script type="text/javascript" src="/js/jquery.js"></script>
	<script type="text/javascript" src="/js/shCore.js"></script>
	<script type="text/javascript" src="/js/shBrushXml.js"></script>
	<link href="/css/shCore.css" type="text/css" rel="stylesheet" />
	<link href="/css/shThemeDefault.css" type="text/css" rel="stylesheet" />

	<script type="text/javascript" src="/js/definition.json"></script>
	<script type="text/javascript">
	    newLine = '\r\n';

		currentElementName = "";
		currentElementMethods = "";
		currentMethodName = "";

		$(document).ready(function(){
			SyntaxHighlighter.highlight();
			// Load up all the API Calls
			$.each(functions, function(key, val) {
				$('#functions').append('<li><a class="functions" href="#" alt="' + key + '">' + key + '</a></li>');
			});
			
			$('#sendRequest').click(function() {
                makeServerRequest();
    		    return false;
    		});
    		
    		$('#previousUsers').click(function() {
    		    $('#previousUserList').toggle();

    			$.ajax({
    				type: "Get",
    				url: '/request/listUsers',
    				success: function(users) {
    				    $('#previousUserList').html('');
    				    
                        for (var i=0; i < users.length; i++) {
                            $('#previousUserList').append('<tr>' + 
                                '<td class="url">' + users[i].url + '</td>' +
                                '<td class="token">' + users[i].token + '</td>' +
                            '</tr>')
                        }
    				}
    			});
    			return false;
    		});
		});
		
		// Capture the API Call selection
		$('#previousUserList tr').live("click", function() {
		    $('#previousUserList').toggle();
            $('#apiURL').val($('td.url', this).text());
            $('#apiToken').val($('td.token', this).text());

			return false;
		});		


		// Capture the API Call selection
		$('a.functions').live("click", function() {

			$('a.functions').removeClass("selected");
			$(this).addClass("selected");

			//Get the selected element
			currentElementName = $(this).attr("alt");
			currentElementMethods = functions[currentElementName];

			// Clear any methods/functions and add the new ones
			$('#methods').html("");	
			$('#fields').html("");
			$.each(currentElementMethods, function(key, val) {
				$('#methods').append('<li><a class="methods" href="#" alt="' + key + '">' + key + '</a></li>');
			});

			return false;
		});


		// Capture the Method Selection
		$('a.methods').live("click", function() {

			$('a.methods').removeClass("selected");
			$(this).addClass("selected");

			//Extract the fields from the selected method
			currentMethodName = $(this).attr("alt");
			$('#fields').html(exploreFields(currentElementMethods[currentMethodName]));

			$('#currentCurlCommand').html(currentElementName + '.' + currentMethodName);

            var code = createRequest();
            displayCode('request', code);
            
			$('#fields input:first').focus();

			return false;
		});

		// Update the curl command on every text change
		$('input.fields').live("change", function() {
            var code = createRequest();
            displayCode('request', code);
		});


		// Recursively traverses the json object building the html form
		function exploreFields(root) {
			var fields = "";

			$.each(root, function(key, val) {
				if (val._text == undefined) {
					fields += '<div class="fields" alt="' + key + '">';
					fields += '<h3>' + key + '</h3>';
					fields += exploreFields(val);
					fields +='</div>';
				} else {
					fields += '<label>' + key + '</label>';
					fields += '<input class="fields" type="text" alt="' + key + '"></input><br/>';
				}
			});

			return fields;
		}

		// Builds the curl command
		function createRequest() {
			var command = "";

			command += '<request method="' + currentElementName + '.' + currentMethodName + '">';
			command += parseFields('#fields', 1);
			command += newLine + '</request>';
			
			return command;
		}

		// Traverses the parent element in the DOM until it reaches the bottom, to build the curl commands
		function parseFields(parent, level) {
		    
			var xml = ""

			var numInputs = 0;
			var numDivFields = 0;
			var tempParseResult = ""

			numInputs = $(parent + ' > input').size();
			numDivFields = $(parent + ' > div').size();

            //Base case with no inputs
			if(numInputs == 0) {
				$.each($(parent + ' > div'), function() {
					tempParseResult = parseFields(parent + '> div', level + 1);

					if (tempParseResult != "") {
						xml += newLine + tabs(level) + '<' + $(this).attr("alt") + '>';
						xml += '' + tempParseResult;
						xml += newLine + tabs(level) + '</' + $(this).attr("alt") + '>';
					}
				});
			
			//Else we have to traverse all the inputs
			} else {
				$.each($(parent + ' > input'), function() {
					if ($(this).val() != "") {
						xml += newLine + tabs(level) + '<' + $(this).attr("alt") + '>';
						xml += $(this).val();
						xml += '</' + $(this).attr("alt") + '>';
					}
				});
                
                //Explore sub sections
				if (numDivFields > 0) {
					$.each($(parent + ' > div'), function() {
						tempParseResult = parseFields(parent + '> div', level + 1);

						if (tempParseResult != "") {
							xml += newLine + tabs(level) + '<' + $(this).attr("alt") + '>';
							xml += '' + tempParseResult;
							xml += newLine + tabs(level) + '</' + $(this).attr("alt") + '>';
						}
					});	
				}
			}

			return xml;
		}
		
		function tabs(count) {
		    var tabs = "";
		    for (var i = 0; i < count; i++) {
		        tabs += '\t';
		    }
		    
		    return tabs;
		}
		
		function makeServerRequest() {
		    var apiURL = $('#apiURL').val().trim();
		    var apiToken = $('#apiToken').val().trim();
		    
		    if (apiURL != "" && apiToken != "") {
                $('#response').hide();
                $('#loader').show();
            
    			$.ajax({
    				type: "POST",
    				url: '/request/index',
    				data: {
    				    url: apiURL,
    				    token: apiToken,
    				    xml: createRequest()
    				},
    				success: function(xml) {
                        $('#loader').hide();
    				    displayCode('response', xml.response);
    				}
    			});
    		} else {
    		    alert("Whoopsie Doodles! Don't forget to give me your API URl and Token!");
    		}
			

		}
		
		function displayCode(sectionID, code) {
		    var sectionJQ = "#" + sectionID;
		    var parent = $(sectionJQ).parent();

			$(sectionJQ).remove();
	        $(parent).append('<pre id="' + sectionID + '" class="brush: xml; toolbar: false; auto-links:false;"></pre>');
			$(sectionJQ).append(code);

			SyntaxHighlighter.highlight();
		}
		


	</script>
</%def>

<%def name="header()">
	<img src="/media/easyAPI.png" id="logo"/>
</%def>

<%def name="sidebar()">
	<h2>API Calls</h2>
	<ul id="functions"></ul>
	<div class="clearfix"></div>

	<h2>Methods</h2>
	<ul id="methods"></ul>
	<div class="clearfix"></div>
	
	<h2>Fields</h2>
	<div id="fields" class="fields"></div>
    <div class="clearfix"></div>

</%def>

<%def name="content()">
	<h2>User</h2>
	<label>API URL:</label> <input id="apiURL" type="text"/><br/><br/>
	<label>API Token:</label> <input id="apiToken" type="text"/><br/><br/>
	
	<a href="#" id="previousUsers">Select Previous Users</a>
	<table id="previousUserList">
	</table>
	<br/>
	
	<div id="apiRequest">
    	<h2>Request</h2>
    	<pre id="request" class="brush: xml; toolbar: false; auto-links:false;">
    	</pre>
	</div>

	<a href="#" id="sendRequest">Send Request</a>
	
	<div id="apiResponse">
		<h2>Response</h2>
		<div id="loader">
		    <img src="/media/ajax-loader.gif"/></br>
		    <p>Shhh! I&apos;m thinking!</p>
		</div>
    	<pre id="response" class="brush: xml; toolbar: false; auto-links:false;">
    	</pre>
	</div>
</%def>
