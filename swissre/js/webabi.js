
web3 = new Web3(new Web3.providers.HttpProvider('https://ropsten.infura.io'));

var county = function(){
  var address = '0x7698cd50ce758b28c9101336c9e8565feb4c3f02';
  var abi = [{"constant":true,"inputs":[{"name":"","type":"bytes32"}],"name":"counties","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"drougInsurancePayout","outputs":[],"payable":false,"type":"function"}];
  var contract = web3.eth.contract(abi).at(address);
  var county = document.getElementById('counties').value;

  contract.counties.call(county, function(e,r){
    console.log(r.toNumber());
    document.getElementById('countyData').innerHTML = r.toNumber();
  })
}
