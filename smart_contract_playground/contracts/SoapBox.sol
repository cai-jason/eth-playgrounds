pragma solidity ^0.5.16;
contract SoapBox {
	// Our 'dict' of addresses that are approved to share opinions
	mapping (address => bool) approvedSoapboxer;
	string opinion;

	// Our event to announce an opinion on the blockchain
	event OpinionBroadcast(address _soapboxer, string _opinion);

	// Constructor function. Name matches the contract
	constructor() public {
	}

	// Because this function is 'payable' it will be called when ether is sent
	// to the contract address.
	function() external payable {
		// msg is a special variable that contains information about the
		// transaction.
		if (msg.value > 20000000000000000) {
			// if the value sent greater than 0.02 ether (in Wei)
			// then add the sender's address to approvedSoapboxer
			approvedSoapboxer[msg.sender] = true;
		}
	}

	// Our read-only function that checks whether the specified address is
	// approved to post opinions. 
	function isApproved(address _soapboxer) public view returns(bool approved) {
		return approvedSoapboxer[_soapboxer];
	}

	// Read-only function that returns the current opinion.
	function getCurrentOpinion() public view returns(string memory) {
		return opinion;
	}

	// Our function that modifies the state on the blockchain.
	function broadcastOpinion(string memory _opinion) public returns (bool success) {
		// Looking up the address of the sending will return false if the sender
		// isn't approved
		if (approvedSoapboxer[msg.sender]) {
			opinion = _opinion;
			emit OpinionBroadcast(msg.sender, opinion);
			return true;
		} else {
			return false;
		}
	}
}
