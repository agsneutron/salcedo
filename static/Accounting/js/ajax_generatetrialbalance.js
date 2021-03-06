/**
 * Created by ariaocho on 18/12/17.
 */

var $j = jQuery.noConflict();
var chk = "0";

$j(document).on('ready', main);

function main(){
     $j('#generatetrialbalance').on('click', search);

    $('input[name="only_with_transactions"]').on('click', function(){
        if ( $(this).is(':checked') ) {
           chk = 1;
        }
        else {
            chk= 0;
        }
    });
}

//Balanza de Comprobación: /accounting/generate_trial_balance
//lower_account_number = Entero
//upper_account_number = Entero
//fiscal_period_year = Entero
//fiscal_period_month = Entero
//title = String
//only_with_transactions = [ 1(True) or 0(False)]
function search() {
     var lower_account_number = $j("#lower_account_number").val();
    var upper_account_number = $j("#upper_account_number").val();
    var fiscal_period_year = $j("#fiscal_period_year").val();
    var fiscal_period_month = $j("#fiscal_period_month").val();
    var title = $j("#title").val();
    var internal_company = $j("#internal_company").val();
    var only_with_transactions = $j("#only_with_transactions").val();
    var url = "/accounting/generate_trial_balance?";


    if (lower_account_number =="" || upper_account_number =="" || fiscal_period_year == "" || fiscal_period_month == "" ){
        message = 'Favor de capturar todos los datos para generar la Balanza \n';
            $('#alertModal').find('.modal-body p').text(message);
            $('#alertModal').modal('show')
    }
    else {

        if (lower_account_number.toString() != "") {
            url = url + "lower_account_number=" + lower_account_number.toString() + "&";
        }
        if (upper_account_number.toString() != "") {
            url = url + "upper_account_number=" + upper_account_number.toString() + "&";
        }
        if (fiscal_period_year.toString() != "") {
            url = url + "fiscal_period_year=" + fiscal_period_year.toString() + "&";
        }
        if (fiscal_period_month.toString() != "") {
            url = url + "fiscal_period_month=" + fiscal_period_month.toString() + "&";
        }
        if (title.toString() != "") {
            url = url + "title=" + title.toString() + "&";
        }
        if (internal_company.toString() != "") {
            url = url + "internal_company=" + internal_company.toString() + "&";
        }

        if (only_with_transactions.toString() != "") {
            url = url + "only_with_transactions=" + chk.toString() + "&";
        }

        //alert(url);
        window.location.href = url;
        //searchengine(url);
    }
}




function searchengine(url) {
    // Setup CSRF tokens and all that good stuff so we don't get hacked
    $.ajaxSetup(
        {
            beforeSend: function (xhr, settings) {
                if (settings.type == "POST")
                    xhr.setRequestHeader("X-CSRFToken", $('[name="csrfmiddlewaretoken"]').val());
                if (settings.type == "GET")
                    xhr.setRequestHeader("X-CSRFToken", $('[name="csrfmiddlewaretoken"]').val());
            }
        }
    );

    // Get an Oauth2 access token and then do the ajax call, because SECURITY
    /*  $.get('/obras/register_by_token', function(ans) {
     var ajaxData = { access_token: ans.access_token};
     //alert(ans.access_token);*/
    var message="";

    $.ajax({
        url: url,
        type: 'get',
        success: function (data) {
            //console.log(data);
           // displayResults(data);

        },
        error: function (data) {

            /*alert('error!! ' + data.status);*/
            /* alert('Ocurrió un error al configurar el proyecto, favor de informar al administrador del sistema el siguiente código de error: ' + data.status);*/
            message = 'Ocurrió un error al realizar la búsqueda, favor de informar al administrador del sistema el siguiente código de error:\n' + data.status;
            $('#alertModal').find('.modal-body p').text(message);
            $('#alertModal').modal('show')

        }
    });


    /* });*/
}

function displayResults(data){
    var sHtml="";
    var sTable="";

    $j('#divTable').html("<div></div>");
    sHtml ='<table class="table-filtros table table-striped table_s" cellspacing="0" width="100%" id="tablaResultados">'
            + ' <colgroup>'
                +' <col width="15%">'
                +' <col width="7%">'
                +' <col width="14%">'
                +' <col width="14%">'
                +' <col width="14%">'
                +' <col width="14%">'
                +' <col width="29%">'
                +' </colgroup>';

    sTable= '<thead>'
                        +'<tr>'
                            +'<th>Nombre</th>'
                            +'<th>No.</th>'
                            +'<th>Nivel</th>'
                            +'<th>Rubro</th>'
                            +'<th>Subcuenta</th>'
                            +'<th>Naturaleza</th>'
                            +'<th>Cód. Agrupador SAT</th>'
                        +'</tr>'
                    +'</thead>'
                    +'<tbody>';

    for (var i = 0; i < data.length; i++) {
            sTable += '<tr>'
            + '<td class="result1 selectable">'+ data[i].name + '</td>'
            + '<td class="result1 selectable">'+ data[i].number + '</td>'
            + '<td class="result1 selectable">'+ data[i].level + '</td>'
            + '<td class="result1 selectable">'+ data[i].item + '</td>'
            + '<td class="result1 selectable">'+ data[i].subsidiary_account + '</td>'
            + '<td class="result1 selectable">'+ data[i].nature_account + '</td>'
            + '<td class="result1 selectable">'+ data[i].grouping_code + '</td>'
            + '</tr>'
    }

    sTable +='</tbody>'
          +'</table>';

    sHtml +=sTable;

    sScript='<script id="js" type="text/javascript"  class="init">'
	        +'$("#tablaResultados").DataTable( {'
            + 'destroy: true,';

    sTable ='columnDefs: ['
             +'       {'
             +'           className: "mdl-data-table__cell--non-numeric"'
             +'       }'
             +'   ],'

             +'   responsive: true,'
             +'   "bInfo": false,';

    sScript += sTable;
    sScript +=' "pageLength": 6,';

    sTable = '   "bLengthChange": false,'
             +'   "language": {'
             +'       "sProcessing": "Procesando...",'
             +'       "sLengthMenu": "Mostrar _MENU_ registros",'
             +'       "sZeroRecords": "No se encontraron resultados",'
             +'       "sEmptyTable": "La consulta no generó resultados a mostrar",'
             +'       "sInfo": "",'
             +'       "sInfoEmpty": "",'
             +'       "sInfoFiltered": "(filtrado de un total de _MAX_ registros)",'
             +'       "sInfoPostFix": "",'
             +'       "sSearch": "",'
             +'      "sUrl": "",'
             +'       "sInfoThousands": ",",'
             +'       "sLoadingRecords": "Cargando...",'
             +'       "oPaginate": {'
             +'           "sFirst": "Primero",'
             +'           "sLast": "Último",'
             +'          "sNext": ">",'
             +'           "sPrevious": "<"'
          +'}'
          +'},'
	      +'} );'
          +'</script>';

    sScript += sTable;

    $j('#divTable').html(sHtml+sScript);

}
