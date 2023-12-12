/*---------------------------
# script extended to all pages
------------------------------
*/
// 1)script to confirm save changes (if exists)
$(document).ready(function () {
    $("#btn-back").click(function () {
        let product = $('#product').val();
        let purchase = $('#purchase').val();
        let sale = $('#sale').val();
        let qty = $('#qty').val();
        let gender = $('#gender').val();
        let note = $('#note').val();

        //hidden input

        let product2 = $('#product2').val();
        let purchase2 = $('#purchase2').val();
        let sale2 = $('#sale2').val();
        let qty2 = $('#qty2').val();
        let gender2 = $('#gender2').val();
        let note2 = $('#note2').val();
        if ((product != product2) || (purchase != purchase2) || 
        (sale != sale2) || (qty != qty2) || (gender != gender2)
        (note2!=note)) {
            $('#modal-confirm').trigger('click');
            return false;
        }
    })
})


/* disable button statement */
$('#product','#product2').on("keyup",function(){
    $(".btn-action").prop("disabled",false);
    if(($("#product").val()==($("#product2").val()))){
        $(".btn-action").prop("disabled",false);
    }
});

$('#purchase','#purchase2').on("keyup",function(){
    $(".btn-action").prop("disabled",false);
    if(($("#purchase").val()==($("#purchase2").val()))){
        $(".btn-action").prop("disabled",false);
    }
});

$('#sale','#sale2').on("keyup",function(){
    $(".btn-action").prop("disabled",false);
    if(($("#sale").val()==($("#sale2").val()))){
        $(".btn-action").prop("disabled",false);
    }
});

$('#qty','#qty2').on("keyup",function(){
    $(".btn-action").prop("disabled",false);
    if(($("#qty").val()==($("#qty2").val()))){
        $(".btn-action").prop("disabled",false);
    }
});

$('#note','#note2').on("keyup",function(){
    $(".btn-action").prop("disabled",false);
    if(($("#note").val()==($("#note2").val()))){
        $(".btn-action").prop("disabled",false);
    }
});

$(document).ready(function(){
    $('.btn-action'.prop('disabled',true));
    $('#gender','gender2').change(function(){
        if(($("#gender").val()==($("#gender").val()))){
            $(".btn-action").attr("disabled","disabled");
        }
        else{
            $(".btn-action").removeAttr("disabled","disabled"); 
        }
    })
})