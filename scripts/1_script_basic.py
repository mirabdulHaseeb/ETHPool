from brownie import accounts, MockERC20, ETHPoolFarm, ETHPoolToken

def main():

    owner, alice, bob = accounts[:3]
    mock_dai = MockERC20.deploy("MockDai", "mDAI", {'from': owner})

    mock_dai.mint(owner, 25000, {'from': owner})
    mock_dai.mint(alice, 25000, {'from': owner})
    mock_dai.mint(bob, 25000, {'from': owner})

    ethPool_tkn = ETHPoolToken.deploy({'from': owner})
    ethPool_frm = ETHPoolFarm.deploy(mock_dai.address, ethPool_tkn.address, {'from': owner})

    print("Owner's dai: ", mock_dai.balanceOf(owner))
    print("Alice's dai: ",mock_dai.balanceOf(alice))
    print("Bob's dai: ",mock_dai.balanceOf(bob))

    mock_dai.approve(ethPool_frm.address, 100, {'from': alice})
    mock_dai.approve(ethPool_frm.address, 200, {'from': bob})

    ethPool_frm.stake(100, {'from': alice})
    ethPool_frm.stake(200, {'from': bob})

    print("Staking Balance - Alice: ", ethPool_frm.stakingBalance(alice))
    print("Staking Balance - Bob: ", ethPool_frm.stakingBalance(bob))

    print("Contract Balance: ", mock_dai.balanceOf(ethPool_frm.address))
