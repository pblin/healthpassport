<script src="http://rawgit.com/ethereum/web3.js/0.16.0/dist/web3.min.js"></script>
<script type="text/javascript">
	
//session
var curOwner = '';
	
//onload	
window.addEventListener('load', function() {
	// Checking if Web3 has been injected by the browser (Mist/MetaMask)
	if (typeof web3 !== 'undefined') {
		// Use Mist/MetaMask's provider
		web3 = new Web3(web3.currentProvider);
	} else {
		console.log('No web3? You should consider trying MetaMask!')
		// fallback - use your fallback strategy (local node / hosted node + in-dapp id mgmt / fail)
		//web3 = new Web3(new Web3.providers.HttpProvider("https://ropsten.infura.io/jusRhRm9lPsVCXFLnnNk"));
		web3 = new Web3(new Web3.providers.HttpProvider("http://52.170.203.132/"));
		
	}

	// Now you can start your app & access web3 freely:
	startApp();
});	


//init web3
function initWeb3 (){

/* 	// Checking if Web3 has been injected by the browser (Mist/MetaMask)
	if (typeof web3 !== 'undefined') {
		// Use Mist/MetaMask's provider
		web3 = new Web3(web3.currentProvider);
	} else {
		console.log('No web3? You should consider trying MetaMask!')
		// fallback - use your fallback strategy (local node / hosted node + in-dapp id mgmt / fail)
		web3 = new Web3(new Web3.providers.HttpProvider("https://ropsten.infura.io/jusRhRm9lPsVCXFLnnNk"));
	} */
}

		
//onload
//window.addEventListener('load', function() {
function startApp(){			
	console.error("startup");
	

		
		
/* 	}).catch((error) => {
	  // null
	}); */
	
}	
	
</script>