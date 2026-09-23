# ============================================================
# CONCRETE COMPRESSIVE STRENGTH PREDICTION
# STREAMLIT APPLICATION
# ============================================================

import streamlit as st
import pandas as pd
import joblib


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Concrete Strength Prediction",
    page_icon="🏗️",
    layout="centered"
)


# ============================================================
# LOAD MODEL
# ============================================================

MODEL_PATH = "best_concrete_strength_model.pkl"
SCALER_PATH = "concrete_scaler.pkl"

try:
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)

except Exception as e:

    st.error("Unable to load the trained model or scaler.")

    st.write("Please make sure these files are present:")
    st.code(
        "best_concrete_strength_model.pkl\n"
        "concrete_scaler.pkl"
    )

    st.stop()


# ============================================================
# TITLE
# ============================================================

st.title("🏗️ Concrete Compressive Strength Prediction")

st.write(
    """
    This application predicts the **compressive strength of concrete**
    using a trained Machine Learning regression model.
    """
)

st.divider()


# ============================================================
# INPUT SECTION
# ============================================================

st.subheader("Enter Concrete Composition")


col1, col2 = st.columns(2)


with col1:

    cement = st.number_input(
        "Cement (kg/m³)",
        min_value=0.0,
        value=350.0,
        step=1.0
    )

    blast_furnace_slag = st.number_input(
        "Blast Furnace Slag (kg/m³)",
        min_value=0.0,
        value=100.0,
        step=1.0
    )

    fly_ash = st.number_input(
        "Fly Ash (kg/m³)",
        min_value=0.0,
        value=50.0,
        step=1.0
    )

    water = st.number_input(
        "Water (kg/m³)",
        min_value=0.0,
        value=180.0,
        step=1.0
    )


with col2:

    superplasticizer = st.number_input(
        "Superplasticizer (kg/m³)",
        min_value=0.0,
        value=10.0,
        step=0.5
    )

    coarse_aggregate = st.number_input(
        "Coarse Aggregate (kg/m³)",
        min_value=0.0,
        value=1000.0,
        step=1.0
    )

    fine_aggregate = st.number_input(
        "Fine Aggregate (kg/m³)",
        min_value=0.0,
        value=700.0,
        step=1.0
    )

    age = st.number_input(
        "Age (days)",
        min_value=1,
        value=28,
        step=1
    )


st.divider()


# ============================================================
# PREDICTION BUTTON
# ============================================================

if st.button(
    "🔍 Predict Concrete Strength",
    use_container_width=True
):

    # --------------------------------------------------------
    # CREATE INPUT DATAFRAME
    # --------------------------------------------------------

    input_data = pd.DataFrame({
        "Cement": [cement],
        "Blast_Furnace_Slag": [blast_furnace_slag],
        "Fly_Ash": [fly_ash],
        "Water": [water],
        "Superplasticizer": [superplasticizer],
        "Coarse_Aggregate": [coarse_aggregate],
        "Fine_Aggregate": [fine_aggregate],
        "Age": [age]
    })


    # --------------------------------------------------------
    # PREDICTION
    # --------------------------------------------------------

    try:

        # Determine whether model needs scaling
        model_name = type(model).__name__

        if model_name in [
            "LinearRegression",
            "SVR",
            "Pipeline"
        ]:

            input_scaled = scaler.transform(input_data)

            prediction = model.predict(
                input_scaled
            )

        else:

            prediction = model.predict(
                input_data
            )


        predicted_strength = float(prediction[0])


        # ----------------------------------------------------
        # DISPLAY RESULT
        # ----------------------------------------------------

        st.success("Prediction completed successfully!")

        st.subheader("Predicted Concrete Strength")

        st.metric(
            label="Compressive Strength",
            value=f"{predicted_strength:.2f} MPa"
        )


        # ----------------------------------------------------
        # INTERPRETATION
        # ----------------------------------------------------

        st.info(
            """
            The predicted value represents the estimated
            compressive strength of the entered concrete mixture.
            """
        )


        # ----------------------------------------------------
        # SHOW INPUT DATA
        # ----------------------------------------------------

        with st.expander("View Input Data"):

            display_data = input_data.copy()

            display_data["Age"] = age

            st.dataframe(
                display_data,
                use_container_width=True
            )


    except Exception as e:

        st.error(
            f"Prediction failed: {str(e)}"
        )


# ============================================================
# PROJECT INFORMATION
# ============================================================

st.divider()

st.subheader("About the Project")

st.write(
    """
    This project uses Machine Learning regression algorithms to
    predict concrete compressive strength from concrete composition
    and curing age.

    The project compares multiple regression models and evaluates
    them using MAE, MSE, RMSE and R².
    """
)

st.caption(
    "Concrete Compressive Strength Prediction using Machine Learning"
)