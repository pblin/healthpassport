contract droughtInsurancePayout {

    mapping(bytes32 => uint) public counties;

    function drougInsurancePayout () {
        counties ['BARINGO'] = 8;
        counties ['BOMET'] = 44;
        counties ['BUNGOMA'] = 41;
        counties ['BUSIA'] = 3;
        counties ['ELGEYO-MARAKWET'] = 1;
        counties ['HOMA-0BAY'] = 0;
        counties ['KAKAMEGA'] = 9;
        counties ['KERICHO'] = 16;
        counties ['KIAMBU'] = 57;
        counties ['KISII'] = 26;
        counties ['KISUMU'] = 0;
        counties ['SIAYA'] = 2;
    }
}
