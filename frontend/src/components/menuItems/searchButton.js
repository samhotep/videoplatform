import React from "react";
import styled from 'styled-components';
import logo from "../../assets/icons8-search-64.png";

function SearchButton(props){
    return (
        <div>
            <ButtonContainer>
                <ButtonImg src={logo} alt="Search"></ButtonImg>
                <ButtonText>Search</ButtonText>
            </ButtonContainer>
        </div>
    )
}

/*
const styles = {
    container: {
        backgroundColor: '#850127',
        padding: 10,
        margin: 10,
        "&:hover": {
            backgroundColor: '#ffffff',
        }
    }
}*/

const ButtonContainer = styled.div`
    display: flex;
    flex-direction: row;
    background: #ffffff;
    border-radius: 15px;
    border: none;
    color: #850127;
`

const ButtonText = styled.div`
    padding: 5px;
    margin: 5px;
`

const ButtonImg = styled.img`
    height: 32px;
    width: 32px;
`

export default SearchButton;
