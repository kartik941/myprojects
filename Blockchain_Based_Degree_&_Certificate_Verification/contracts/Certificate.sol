// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract Certificate {
    struct Cert {
        string studentName;
        string courseName;
        string issuer;
        uint256 dateIssued;
    }

    mapping(uint256 => Cert) public certificates;
    uint256 public certCount;

    event CertificateIssued(uint256 certId, string studentName, string courseName, string issuer);

    function issueCertificate(string memory _studentName, string memory _courseName, string memory _issuer) public {
        certCount++;
        certificates[certCount] = Cert(_studentName, _courseName, _issuer, block.timestamp);
        emit CertificateIssued(certCount, _studentName, _courseName, _issuer);
    }

    function getCertificate(uint256 _certId) public view returns (Cert memory) {
        return certificates[_certId];
    }
}
