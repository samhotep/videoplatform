import React from "react";
//import { TitleBar } from "../components/headers";

function TitleItem(props){
    return (
        <div style={styles.container}>
            {props.name}
        </div>
    )
}

const styles = {
    container: {
        padding: 10,
        margin: 10
    }

}

export default TitleItem;
